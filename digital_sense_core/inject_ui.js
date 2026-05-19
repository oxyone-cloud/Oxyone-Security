// SCRIPT D'INJECTION OXYONE - PROPRIÉTÉ SSCI
(function() {
    console.log("Activation du protocole Digital Sense UI...");

    // 1. Injection du style CSS (que nous avons créé)
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'digital_sense_ui.css'; 
    document.head.appendChild(link);

    // 2. Transformation du bloc Digital Sense
    var dsBlock = document.getElementById('digital-sense'); // On cible votre bloc existant
    if(dsBlock) {
        dsBlock.className = 'digital-sense-container';
        dsBlock.innerHTML = `
            <div class="certification-badge">CERTIFICATION ACTIVE</div>
            <h3>DIGITAL SENSE : DATA VAULT</h3>
            <div class="data-log-view" id="live-logs">
                Connexion au flux de certification en cours...
            </div>
            <div class="berne-mention">© SSCI - Protégé par la Convention de Berne</div>
        `;
    }
})()
