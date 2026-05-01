// ==UserScript==
// @name         Idealista — Pré-remplir message contact (Florent BCN)
// @namespace    https://github.com/SuperCelmar/introduction-to-github
// @version      1.0.0
// @description  Ajoute un bouton "📋 Pré-remplir mon message" sur les annonces Idealista pour insérer un message personnalisé en 1 clic. L'envoi reste manuel.
// @match        https://www.idealista.com/inmueble/*
// @match        https://www.idealista.com/en/inmueble/*
// @match        https://www.idealista.com/fr/inmueble/*
// @match        https://www.idealista.es/inmueble/*
// @run-at       document-idle
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    // -------- À PERSONNALISER --------
    const USER = {
        prenom: 'Florent',
        nom: 'Lin',
        email: '1florentlin@gmail.com',
        tel: '+33 7 81 63 66 63',
        age: 24,
    };

    const MSG = {
        fr: () => `Bonjour, je m'appelle ${USER.prenom} ${USER.nom}, ${USER.age} ans, je commence un VIE de 12 mois chez Hello Pomelo (Carrer de Mallorca 100) le 1er juin. Indemnité 2500–3000 €/mois + garante (ma mère, 5000 €/mois nets). Studio meublé idéal pour moi. Je suis à Barcelone du 17 au 20 mai pour visiter, dispo 9h–21h. Move-in 20–31 mai. Dossier complet (contrat VIE, fiches de paie garante, ID) prêt à envoyer. Pourrions-nous fixer une visite ? Merci ! ${USER.email} — ${USER.tel}`,
        en: () => `Hi, I'm ${USER.prenom} ${USER.nom}, ${USER.age}, starting a 12-month VIE contract at Hello Pomelo (Carrer de Mallorca 100) on June 1st. Net allowance €2,500–3,000/month + guarantor (my mother, €5,000/month net). Looking for a furnished studio. I'll be in Barcelona May 17–20 to visit, available 9am–9pm. Move-in May 20–31. Full dossier (VIE contract, guarantor payslips, ID) ready to send. Could we book a viewing? Thanks — ${USER.email} — ${USER.tel}`,
        es: () => `Hola, soy ${USER.prenom} ${USER.nom}, ${USER.age} años, empiezo un VIE de 12 meses en Hello Pomelo (Carrer de Mallorca 100) el 1 de junio. Asignación 2.500–3.000 €/mes + avalista (mi madre, 5.000 €/mes netos). Busco estudio amueblado. Estaré en Barcelona del 17 al 20 de mayo, disponible 9h–21h. Entrada 20–31 mayo. Dossier completo (contrato VIE, nóminas del avalista, DNI) listo. ¿Podríamos concertar una visita? Gracias — ${USER.email} — ${USER.tel}`,
    };

    // -------- Détection langue --------
    function detectLang() {
        const html = document.documentElement.lang || '';
        if (html.startsWith('en')) return 'en';
        if (html.startsWith('fr')) return 'fr';
        if (html.startsWith('es') || html.startsWith('ca')) return 'es';
        const url = location.pathname;
        if (url.startsWith('/en/')) return 'en';
        if (url.startsWith('/fr/')) return 'fr';
        return 'es';
    }

    // -------- UI --------
    function injectButton() {
        if (document.getElementById('bcn-prefill-btn')) return;

        const btn = document.createElement('button');
        btn.id = 'bcn-prefill-btn';
        btn.textContent = '📋 Pré-remplir mon message';
        btn.style.cssText = `
            position: fixed;
            top: 80px;
            right: 16px;
            z-index: 99999;
            padding: 10px 14px;
            background: #1f9d55;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transition: transform 0.1s, background 0.2s;
        `;
        btn.addEventListener('mouseenter', () => { btn.style.background = '#1a8048'; });
        btn.addEventListener('mouseleave', () => { btn.style.background = '#1f9d55'; });
        btn.addEventListener('click', fillMessage);
        document.body.appendChild(btn);
    }

    function findTextarea() {
        // Idealista utilise un <textarea> dans son module de contact ; sélecteurs tolérants.
        const candidates = [
            'textarea[name="message"]',
            'textarea[name="texto"]',
            'textarea[id*="message"]',
            'textarea[id*="messageContact"]',
            'textarea[placeholder*="mensaje" i]',
            'textarea[placeholder*="message" i]',
            'textarea',
        ];
        for (const sel of candidates) {
            const el = document.querySelector(sel);
            if (el) return el;
        }
        return null;
    }

    function fillMessage() {
        const lang = detectLang();
        const text = MSG[lang]();

        const ta = findTextarea();
        if (!ta) {
            alert(
                "Aucun champ de message trouvé.\n\n" +
                "Ouvre d'abord le formulaire de contact (bouton « Contactar ») " +
                "puis réappuie sur « Pré-remplir mon message »."
            );
            return;
        }

        // Setter natif pour déclencher le re-render React/Vue d'Idealista
        const setter = Object.getOwnPropertyDescriptor(
            window.HTMLTextAreaElement.prototype, 'value'
        ).set;
        setter.call(ta, text);
        ta.dispatchEvent(new Event('input', { bubbles: true }));
        ta.dispatchEvent(new Event('change', { bubbles: true }));

        // Aussi remplir éventuellement les champs nom/email/tel s'ils sont vides
        autofillField(['name', 'nombre', 'firstName'], `${USER.prenom} ${USER.nom}`);
        autofillField(['email', 'correo'], USER.email);
        autofillField(['phone', 'tel', 'telefono'], USER.tel);

        ta.focus();
        ta.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Feedback visuel
        const btn = document.getElementById('bcn-prefill-btn');
        if (btn) {
            const original = btn.textContent;
            btn.textContent = '✅ Inséré — relis et envoie';
            btn.style.background = '#16855e';
            setTimeout(() => {
                btn.textContent = original;
                btn.style.background = '#1f9d55';
            }, 2500);
        }
    }

    function autofillField(nameKeywords, value) {
        for (const kw of nameKeywords) {
            const el = document.querySelector(
                `input[name*="${kw}" i], input[id*="${kw}" i], input[placeholder*="${kw}" i]`
            );
            if (el && !el.value) {
                const setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value'
                ).set;
                setter.call(el, value);
                el.dispatchEvent(new Event('input', { bubbles: true }));
                el.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }
    }

    // Idealista charge des composants en async — on tente plusieurs fois
    injectButton();
    const obs = new MutationObserver(() => injectButton());
    obs.observe(document.body, { childList: true, subtree: true });
})();
