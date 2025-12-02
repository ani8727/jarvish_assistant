// Minimal shim for Eel when serving the frontend as a static site
// This prevents 404 for /eel.js on static hosts (Vercel) and
// provides stub implementations for functions the UI calls.

(function (global) {
    if (global.eel) return; // don't overwrite real eel if present

    var eel = {};

    // store exposed JS functions (no-op in static mode)
    eel._exposed = {};

    // mimic eel.expose(fn) used in controller.js — store by name
    eel.expose = function (fn) {
        try {
            if (typeof fn === 'function' && fn.name) {
                eel._exposed[fn.name] = fn;
            }
        } catch (e) { /* ignore */ }
    };

    // Calls from frontend that normally call Python. In static mode
    // we implement simple local behavior so UI remains usable.
    eel.playAssistantSound = function () {
        console.log('eel.playAssistantSound() shim called');
        // mimic brief listening UI update if controller functions exist
        if (typeof global.ShowHood === 'function') {
            try { global.ShowHood(); } catch (e) { }
        }
        if (typeof global.DisplayMessage === 'function') {
            try { global.DisplayMessage('Listening...'); } catch (e) { }
        }
    };

    eel.allCommands = function (message) {
        console.log('eel.allCommands() shim called, message=', message);
        var userMsg = message || '';
        try {
            if (userMsg && typeof global.senderText === 'function') {
                global.senderText(userMsg);
            }
            var response = userMsg ? "Assistant (local): I heard '" + userMsg + "'" : 'Assistant (local): Hello — say something!';
            if (typeof global.receiverText === 'function') {
                global.receiverText(response);
            }
            if (typeof global.DisplayMessage === 'function') {
                global.DisplayMessage(response);
            }
        } catch (e) {
            console.warn('eel shim failed to call UI handlers', e);
        }

        // return a promise-like object to be somewhat compatible with Eel
        return function () { return Promise.resolve(); };
    };

    // no-op for other Eel methods used in some projects
    eel._call = function () { console.log('eel._call shim'); };

    // attach to global
    global.eel = eel;
})(window);
