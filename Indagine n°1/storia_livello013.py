# Storia interattiva delle Backrooms - Livello 013
# La Stanza delle Opportunità Perse

contenuto_storia_livello013 = {
    'inizio': {
        'testo': """L'ultima porta della Biblioteca Infinita si chiude alle mie spalle con un tonfo definitivo. Mi ritrovo in uno spazio circolare immenso, le pareti coperte di porte di ogni epoca e stile. Alcune sono moderne, altre antiche come il tempo stesso. Ma è la porta centrale, dorata e maestosa, ad attirare immediatamente la mia attenzione. L'aria è densa di rimpianto, e un sussurro appena percettibile riecheggia nell'ambiente: "Mike... ricordi le tue scelte?" Le porte iniziano a pulsare debolmente, ognuna chiamandomi con memorie che preferirei dimenticare.""",
        'scelte': [
            {'id': 'esplora_porte', 'testo': 'Esplorare le porte circostanti'},
            {'id': 'esamina_dorata', 'testo': 'Esaminare la porta dorata centrale'},
            {'id': 'ascolta_sussurri', 'testo': 'Prestare attenzione ai sussurri'}
        ]
    },
    'esplora_porte': {
        'testo': """Mi avvicino alle porte. Ognuna emana un'energia diversa, un richiamo personale. La prima mostra una scena del Livello 3, dove ho iniziato a seguire le tracce di Josh. Vedo me stesso ignorare un dettaglio cruciale, un simbolo che avrebbe potuto salvarlo. La seconda porta riflette il Livello 6, l'oscurità dove ho perso Edward. La terza... la terza mostra la neve eterna del Livello 14, dove Sasha è scomparsa. La Presenza Invisibile sussurra: "Ogni porta è una scelta sbagliata. Ogni memoria un fallimento." """,
        'scelte': [
            {'id': 'porta_josh', 'testo': 'Aprire la porta del Livello 3'},
            {'id': 'porta_edward', 'testo': 'Aprire la porta del Livello 6'},
            {'id': 'porta_sasha', 'testo': 'Aprire la porta del Livello 14'}
        ]
    },
    'porta_josh': {
        'testo': """La porta si apre sul Livello 3. Le luci fluorescenti ronzano come sempre, ma la scena è distorta, sbagliata. Vedo Josh che studia i simboli sulla parete, ma questa volta noto dettagli che prima mi erano sfuggiti. "Potevi salvarlo," sussurra la Presenza, "bastava guardare più attentamente." I simboli sulla parete formano un pattern che ora riconosco - un avvertimento, non un invito. La colpa mi schiaccia mentre la porta si chiude alle mie spalle.""",
        'scelte': [
            {'id': 'analizza_simboli', 'testo': 'Studiare i simboli più attentamente'},
            {'id': 'cerca_josh', 'testo': 'Tentare di raggiungere Josh'},
            {'id': 'accetta_fallimento', 'testo': 'Accettare il fallimento passato'}
        ]
    },
    'porta_edward': {
        'testo': """L'oscurità del Livello 6 mi avvolge, ma questa volta è diversa - viva, accusatoria. Rivivo il momento in cui ho perso Edward, ma ora vedo le ombre che si muovevano con uno scopo, non per minacciare. "Lui aveva capito," mormora la Presenza, "ma tu hai scelto la paura invece della comprensione." L'oscurità prende forma, mostrando infinite possibilità alternative, tutte ora irraggiungibili.""",
        'scelte': [
            {'id': 'segui_ombre', 'testo': 'Seguire le ombre senzienti'},
            {'id': 'chiama_edward', 'testo': 'Chiamare disperatamente Edward'},
            {'id': 'studia_oscurita', 'testo': 'Studiare la vera natura dell\'oscurità'}
        ]
    },
    'porta_sasha': {
        'testo': """Il gelo del Livello 14 mi penetra fino alle ossa, ma non è il freddo fisico a farmi tremare. Vedo Sasha che studia i cristalli di memoria, cercando di comunicare una verità che ho ignorato. "Lei aveva trovato la chiave," sibila la Presenza, "ma tu eri troppo concentrato a cercare risposte sbagliate." I cristalli di ghiaccio riflettono infinite versioni di quel momento, ognuna un rimpianto cristallizzato.""",
        'scelte': [
            {'id': 'esamina_cristalli', 'testo': 'Esaminare i cristalli di memoria'},
            {'id': 'raggiungi_sasha', 'testo': 'Tentare di raggiungere Sasha'},
            {'id': 'decodifica_messaggio', 'testo': 'Decodificare il suo ultimo messaggio'}
        ]
    },
    'esamina_dorata': {
        'testo': """La porta dorata pulsa con una luce ipnotica. Riflette non solo la mia immagine, ma tutte le versioni di me stesso che avrebbero potuto essere. "Questa è la tua ultima scelta," dice la Presenza, la sua voce ora chiara come cristallo. "Oltre questa porta c'è la verità che hai sempre cercato... o forse, la bugia che ti racconti." La superficie dorata ondeggia, mostrandomi flash di tutti i livelli che ho attraversato, tutte le vite che ho toccato e perso.""",
        'scelte': [
            {'id': 'apri_dorata', 'testo': 'Aprire la porta dorata'},
            {'id': 'rifiuta_dorata', 'testo': 'Rifiutare la tentazione'},
            {'id': 'cerca_alternativa', 'testo': 'Cercare un\'altra via d\'uscita'}
        ]
    },
    'ascolta_sussurri': {
        'testo': """I sussurri si intensificano, diventando una cacofonia di voci familiari. Josh parla di simboli viventi, Edward descrive l'oscurità senziente, Sasha rivela segreti congelati nel tempo. Ma è un'altra voce a emergere - la mia stessa voce, che elenca ogni errore, ogni momento di esitazione, ogni opportunità sprecata. "Non sei qui per caso," dice la Presenza, "sei qui perché ogni tua scelta ti ha condotto inevitabilmente a questo momento." """,
        'scelte': [
            {'id': 'confronta_voci', 'testo': 'Confrontare le voci dei dispersi'},
            {'id': 'analizza_errori', 'testo': 'Analizzare i propri errori'},
            {'id': 'cerca_redenzione', 'testo': 'Cercare una possibilità di redenzione'}
        ]
    },
    'apri_dorata': {
        'testo': """La porta dorata si apre con un suono cristallino, rivelando... il vuoto. Non l'oscurità del Livello 6 o il gelo del Livello 14, ma il puro, assoluto nulla. "Questa è la verità che cercavi," risuona la Presenza, "il vuoto che hai sempre temuto di trovare." Mentre il vuoto mi attira inesorabilmente, vedo flash di comprensione: le Backrooms non sono un labirinto da cui fuggire, ma uno specchio delle nostre paure più profonde. Josh, Edward, Sasha... non sono scomparsi, si sono trasformati. E ora... ora è il mio turno.""",
        'scelte': []
    },
    'rifiuta_dorata': {
        'testo': """Tento di resistere al richiamo della porta dorata, ma le pareti della stanza iniziano a contrarsi. Le altre porte svaniscono una ad una, lasciandomi solo con le mie scelte sbagliate e la porta dorata. "Non c'è rifiuto," tuona la Presenza, "solo accettazione." Il pavimento sotto di me si dissolve, e mentre cado nel vuoto eterno, capisco: non sono mai stato un investigatore delle Backrooms... sono sempre stato parte del loro disegno.""",
        'scelte': []
    },
    'cerca_alternativa': {
        'testo': """Disperatamente, cerco un'altra via d'uscita. Ma ogni passo che faccio mi riporta davanti alla porta dorata. Le pareti sussurrano con le voci di tutti coloro che ho perso, e ogni sussurro è un'accusa. "Non esiste alternativa," dice la Presenza, "solo il ciclo eterno delle scelte e delle loro conseguenze." La stanza stessa sembra respirare, pulsare con una consapevolezza antica. E finalmente capisco: non sono mai stato io a investigare le Backrooms... sono le Backrooms che hanno investigato me.""",
        'scelte': []
    },
    'finale_disperazione': {
        'testo': """Le pareti della Stanza delle Opportunità Perse tremano con una risata cosmica. Ogni porta si spalanca simultaneamente, rivelando infinite versioni dei miei fallimenti. La porta dorata al centro pulsa con una luce insostenibile. "Benvenuto alla verità," tuona la Presenza, ora manifestandosi come un vortice di pura consapevolezza. "Non sei il primo a cercare risposte, e non sarai l'ultimo a diventare parte della domanda." Mentre la mia coscienza si dissolve nel vuoto eterno, l'ultimo pensiero è una realizzazione terribile: le Backrooms non sono un luogo... sono uno stato dell'essere, e io sono sempre stato destinato a diventare parte di esse.""",
        'scelte': []
    }
}
