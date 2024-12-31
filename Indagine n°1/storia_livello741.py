# Storia interattiva delle Backrooms - Livello 741
# La Biblioteca Infinita

contenuto_storia_livello741 = {
    'inizio': {
        'testo': """Gli scaffali si estendono in ogni direzione, perdendosi nell'infinito. L'aria è densa di polvere e sapere antico. Sono Mike, e il portale del Leviatano mi ha condotto qui, nel Livello 741 - La Biblioteca Infinita.

Le lampade tremolanti creano ombre danzanti tra i libri, e nell'aria... sussurri. Voci che sembrano provenire dalle pagine stesse, ognuna racconta storie di esploratori perduti nei meandri delle Backrooms.

Su uno scaffale vicino, noto tre libri particolari che sembrano chiamarmi con una forza quasi magnetica. Uno emana una luce fluorescente, un altro sembra assorbire la luce circostante, e il terzo è coperto di brina. Mentre tendo la mano, sento i Custodi Silenziosi muoversi tra gli scaffali, le loro vesti che frusciano nella penombra.""",
        'scelte': [
            {'id': 'esplora_scaffali', 'testo': 'Esplorare gli scaffali vicini'},
            {'id': 'segui_sussurri', 'testo': 'Seguire la fonte dei sussurri'},
            {'id': 'esamina_libri', 'testo': 'Esaminare i tre libri'},
            {'id': 'osserva_custodi', 'testo': 'Osservare i Custodi Silenziosi'}
        ]
    },
    'esamina_libri': {
        'testo': """Mi avvicino ai tre libri. Il primo emana una luce fluorescente simile a quella del Livello 3, il secondo sembra assorbire la luce come l'oscurità del Livello 6, e il terzo è coperto di brina, ricordandomi il gelo del Livello 14. Mentre tendo la mano, le pagine iniziano a sussurrare storie di esploratori perduti: Josh, Edward, Sasha... le loro voci si mescolano in un coro di rivelazioni.""",
        'scelte': [
            {'id': 'libro_luminoso', 'testo': 'Aprire il libro luminoso'},
            {'id': 'libro_oscuro', 'testo': 'Aprire il libro oscuro'},
            {'id': 'libro_gelido', 'testo': 'Aprire il libro gelido'}
        ]
    },
    'libro_luminoso': {
        'testo': """Le pagine brillano di luce propria. Leggo di Josh e della sua trasformazione nel Livello 3, di come le pareti viventi lo abbiano accolto. Ma c'è di più - vedo connessioni, pattern che prima mi sfuggivano. Le luci fluorescenti, le pareti senzienti, tutto parte di un disegno più grande. Un'ombra si muove tra gli scaffali, e sento passi silenziosi avvicinarsi.""",
        'scelte': [
            {'id': 'continua_lettura', 'testo': 'Continuare a leggere nonostante il pericolo'},
            {'id': 'nascondi_libro', 'testo': 'Nascondere il libro e allontanarsi'},
            {'id': 'confronta_ombra', 'testo': 'Affrontare l\'ombra'}
        ]
    },
    'libro_oscuro': {
        'testo': """L'oscurità del libro sembra viva, proprio come quella del Livello 6. Le pagine raccontano di Edward e del suo incontro con l'oscurità senziente. Ma mentre leggo, le ombre tra gli scaffali si addensano, e scorgo figure incappucciate - i Custodi Silenziosi - che mi osservano da lontano. Il libro rivela verità sulla natura dell'oscurità nelle Backrooms, su come sia un ponte tra dimensioni.""",
        'scelte': [
            {'id': 'approfondisci_oscurita', 'testo': 'Approfondire i segreti dell\'oscurità'},
            {'id': 'evita_custodi', 'testo': 'Cercare di evitare i Custodi'},
            {'id': 'chiedi_permesso', 'testo': 'Tentare di comunicare con i Custodi'}
        ]
    },
    'libro_gelido': {
        'testo': """Il freddo del libro mi penetra nelle ossa, trasportandomi nei ricordi del Livello 14. Le pagine ghiacciate narrano di Sasha e dei cristalli di memoria, ma rivelano anche una verità più profonda sulla natura del ghiaccio eterno - un archivio vivente di tutte le memorie delle Backrooms. Mentre leggo, i corridoi della biblioteca iniziano a spostarsi, riarrangiandosi in pattern impossibili.""",
        'scelte': [
            {'id': 'segui_memoria', 'testo': 'Seguire il filo delle memorie'},
            {'id': 'mappa_movimento', 'testo': 'Cercare di mappare i movimenti'},
            {'id': 'cerca_uscita', 'testo': 'Cercare una via d\'uscita'}
        ]
    },
    'continua_lettura': {
        'testo': """Ignoro il pericolo e continuo a leggere. Le pagine rivelano una mappa impossibile delle Backrooms, mostrando come tutti i livelli siano interconnessi. Il Leviatano, i muri viventi, l'oscurità senziente, il ghiaccio eterno - tutti parte di un organismo cosmico in evoluzione. Ma la conoscenza ha un prezzo: il Librario Arcano emerge dall'ombra, la sua figura incorporea fluttua tra gli scaffali.""",
        'scelte': [
            {'id': 'confronto_librario', 'testo': 'Affrontare il Librario Arcano'},
            {'id': 'cerca_fuga', 'testo': 'Tentare una fuga disperata'},
            {'id': 'offri_scambio', 'testo': 'Proporre uno scambio di conoscenza'}
        ]
    },
    'confronto_librario': {
        'testo': """Il Librario Arcano si manifesta completamente: una figura di pura conoscenza cristallizzata. "Hai letto troppo," risuona la sua voce nella mia mente, "ma non abbastanza per comprendere." Gli scaffali si muovono come onde in un mare di libri, e vedo porte dorate materializzarsi tra loro. "Ogni scelta ha un prezzo," continua il Librario, "e tu hai fatto troppe domande." Una porta in particolare brilla più intensamente delle altre.""",
        'scelte': [
            {'id': 'accetta_destino', 'testo': 'Accettare il giudizio del Librario'},
            {'id': 'sfida_entita', 'testo': 'Sfidare l\'entità'},
            {'id': 'ultima_domanda', 'testo': 'Porre un\'ultima domanda'}
        ]
    },
    'osserva_custodi': {
        'testo': """Mi nascondo tra gli scaffali e osservo i Custodi Silenziosi. Le loro figure incappucciate si muovono con grazia innaturale, come se fluttuassero appena sopra il pavimento. Sotto i cappucci, dove dovrebbero esserci volti, vedo solo oscurità profonda.

Uno di loro si ferma vicino a me, e per un momento terrificante, sento la sua presenza scrutare la mia anima. Non ha occhi visibili, eppure so che mi sta studiando. Nella mia mente, sento una voce antica sussurrare: 'Cercatore di verità, cosa speri di trovare qui? Ogni conoscenza ha il suo prezzo.'""",
        'scelte': [
            {'id': 'parla_custode', 'testo': 'Tentare di comunicare con il Custode'},
            {'id': 'evita_custode', 'testo': 'Allontanarsi silenziosamente'},
            {'id': 'chiedi_conoscenza', 'testo': 'Chiedere della vera natura delle Backrooms'},
            {'id': 'mostra_determinazione', 'testo': 'Mostrare determinazione nel trovare risposte'}
        ]
    },
    'parla_custode': {
        'testo': """Con voce tremante, tento di comunicare: "Cerco risposte sui miei predecessori - Josh, Edward, Sasha..." Il Custode inclina leggermente il capo, e nella mia mente risuonano echi di storie intrecciate: visioni di Josh che si fonde con le pareti del Livello 3, Edward che abbraccia l'oscurità del Livello 6, Sasha che diventa uno con il ghiaccio del Livello 14.

"Le loro storie sono qui," sussurra il Custode nella mia mente, "preservate per l'eternità. Ma la vera domanda è: sei pronto a comprendere il tuo ruolo in questo grande disegno?" """,
        'scelte': [
            {'id': 'chiedi_ruolo', 'testo': 'Chiedere del proprio ruolo'},
            {'id': 'cerca_libri', 'testo': 'Cercare i libri sugli altri esploratori'},
            {'id': 'sfida_custode', 'testo': 'Sfidare il Custode'},
            {'id': 'segui_custode', 'testo': 'Seguire il Custode'}
        ]
    },
    'chiedi_ruolo': {
        'testo': """Il Custode fluttua più vicino, l'aria intorno a noi diventa pesante di significato. "Tu sei l'Archivista," risuona la sua voce nella mia mente, "colui che deve preservare le memorie, testimoniare le trasformazioni. Gli altri hanno trovato i loro ruoli - Josh è diventato Sinapsi, Edward è diventato Sangue, Sasha è diventata Memoria. E tu... tu sei destinato a diventare Storia."

Le scaffalature sembrano contorcersi mentre parla, formando pattern impossibili che ricordano una doppia elica di DNA cosmico. Vedo libri che si scrivono da soli, pagine che raccontano storie ancora in divenire.""",
        'scelte': [
            {'id': 'accetta_destino', 'testo': 'Accettare il ruolo di Archivista'},
            {'id': 'rifiuta_destino', 'testo': 'Rifiutare il destino proposto'},
            {'id': 'cerca_alternative', 'testo': 'Cercare un destino alternativo'},
            {'id': 'chiedi_dettagli', 'testo': 'Chiedere maggiori dettagli sul ruolo'}
        ]
    },
    'accetta_destino': {
        'testo': """Mentre accetto il mio ruolo, sento una trasformazione iniziare. La mia coscienza si espande, toccando ogni libro, ogni storia, ogni memoria preservata in questa biblioteca infinita. Vedo la vera natura delle Backrooms: non un labirinto, ma un archivio vivente di tutte le realtà possibili.

I Custodi Silenziosi si radunano intorno a me, le loro forme ora chiare alla mia nuova percezione: sono altri Archivisti, trasformati come sto per essere io. "C'è un'ultima porta da attraversare," sussurrano all'unisono, "nel Livello 013, dove ogni storia trova il suo vero significato." """,
        'scelte': [
            {'id': 'verso_013', 'testo': 'Procedere verso il Livello 013'},
            {'id': 'ultima_resistenza', 'testo': 'Opporre un\'ultima resistenza'},
            {'id': 'contempla_conoscenza', 'testo': 'Contemplare la vastità della conoscenza'}
        ]
    },
    'verso_013': {
        'testo': """I Custodi mi guidano attraverso corridoi impossibili di libri che si scrivono da soli, ogni pagina una finestra su infinite possibilità. Arriviamo davanti a una porta dorata, ornata di simboli che sembrano muoversi e cambiare significato mentre li osservo.

"Nel Livello 013," sussurrano i Custodi, "affronterai le tue scelte, le tue opportunità perse. Solo allora capirai veramente il tuo ruolo nell'infinito archivio delle Backrooms." La porta si apre, rivelando una luce accecante che sembra chiamarmi.""",
        'scelte': [
            {'id': 'attraversa_porta', 'testo': 'Attraversare la porta verso il Livello 013'},
            {'id': 'ultimo_sguardo', 'testo': 'Dare un ultimo sguardo alla Biblioteca'},
            {'id': 'ultima_domanda', 'testo': 'Porre un\'ultima domanda ai Custodi'}
        ]
    },
    'attraversa_porta': {
        'testo': """Con un ultimo respiro profondo, attraverso la porta dorata. La luce mi avvolge, e sento la mia coscienza espandersi ancora di più. Vedo tutte le storie convergere: Josh nei muri viventi, Edward nell'oscurità senziente, Sasha nel ghiaccio eterno. E ora, mentre entro nel Livello 013, capisco che il mio viaggio non è finito - è solo cambiato.

La Biblioteca Infinita svanisce dietro di me, ma il suo sapere rimane impresso nella mia anima trasformata. Davanti a me si apre il Livello 013 - La Stanza delle Opportunità Perse, dove ogni porta è un ricordo, ogni scelta un rimpianto, ogni momento una lezione da preservare nell'infinito archivio delle Backrooms.""",
        'scelte': []
    },
    'accetta_destino': {
        'testo': """Mentre accetto il giudizio del Librario, le porte dorate si moltiplicano all'infinito, ciascuna che riflette un momento della mia vita, una scelta, un rimpianto. La biblioteca stessa sembra dissolversi, trasformandosi in uno spazio circolare pieno di porte. Il Librario sussurra un'ultima verità: "Hai cercato risposte nelle storie degli altri. Ora è tempo di affrontare la tua." La porta centrale si apre, rivelando il Livello 013 - La Stanza delle Opportunità Perse. Mentre varco la soglia, capisco che il mio viaggio non è finito - è solo cambiato.""",
        'scelte': []
    },
    'sfida_entita': {
        'testo': """Tento di sfidare il Librario, ma è futile. La biblioteca stessa risponde alla sua volontà, i corridoi si contorcono e si trasformano. Mi ritrovo in uno spazio circolare, circondato da porte che mostrano frammenti della mia vita. "Non si può sfuggire alla propria storia," risuona la voce del Librario mentre svanisce. La porta centrale si apre sul Livello 013, e so che non ho altra scelta che attraversarla.""",
        'scelte': []
    },
    'ultima_domanda': {
        'testo': """La mia ultima domanda riecheggia nella biblioteca: "Qual è il vero scopo delle Backrooms?" Il Librario risponde con una risata che fa tremare gli scaffali: "Guardati intorno. Ogni libro, ogni storia, ogni livello - tutti specchi dell'anima umana. E tu... tu sei solo un'altra storia che cerca il suo finale." Lo spazio si trasforma nella Stanza delle Opportunità Perse, e mentre il Livello 013 si materializza davanti a me, capisco che alcune domande portano solo a più domande.""",
        'scelte': []
    }
}