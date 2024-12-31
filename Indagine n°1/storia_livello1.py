# Storia interattiva delle Backrooms - Livello 1
# Le indagini di Mike - M.E.G. Investigator

contenuto_storia_livello1 = {
    'inizio': {
        'testo': """Le luci fluorescenti ronzano sopra la mia testa nell'ufficio del M.E.G., qui nel Livello 1. Mi chiamo Mike, e come investigatore della Major Explorer Group, il mio compito è analizzare e catalogare le sparizioni nelle Backrooms. Sulla mia scrivania si accumula una pila di rapporti inquietanti: resoconti frammentari di esploratori scomparsi, simboli ricorrenti, pattern di sparizioni. Tre casi in particolare hanno attirato la mia attenzione nelle ultime settimane - interconnessi in modi che non riesco ancora a comprendere pienamente.""",
        'scelte': [
            {'id': 'esamina_rapporti', 'testo': 'Esaminare i rapporti sulle sparizioni'},
            {'id': 'consulta_database', 'testo': 'Consultare il database del M.E.G.'},
            {'id': 'ispeziona_mappa', 'testo': 'Studiare la mappa dei livelli'}
        ]
    },
    'esamina_rapporti': {
        'testo': """Sfoglio i rapporti più recenti. Il primo parla di strani simboli fluorescenti trovati nel Livello 3, il secondo documenta ombre viventi nel Livello 6, e l'ultimo descrive impronte nella neve eterna del Livello 14. Ciò che mi inquieta è un pattern ricorrente: in ogni caso, gli esploratori scomparsi sembravano... cambiare, prima di sparire completamente. Le loro ultime comunicazioni diventavano sempre più enigmatiche, come se stessero percependo qualcosa che noi non possiamo comprendere.""",
        'scelte': [
            {'id': 'analizza_pattern', 'testo': 'Analizzare il pattern delle sparizioni'},
            {'id': 'cerca_testimoni', 'testo': 'Cercare possibili testimoni'},
            {'id': 'studia_simboli', 'testo': 'Esaminare i simboli ricorrenti'}
        ]
    },
    'consulta_database': {
        'testo': """Il database del M.E.G. lampeggia sul mio terminale mentre inserisco i parametri di ricerca. Tre nomi appaiono evidenziati in rosso, contrassegnati come "Status: Scomparso - Possibile Assimilazione". I rapporti medici pre-sparizione mostrano anomalie neurologiche comuni: modelli cerebrali alterati, percezione distorta dello spazio-tempo. Come se le loro menti si stessero... espandendo verso qualcosa di più vasto.""",
        'scelte': [
            {'id': 'analizza_dati', 'testo': 'Analizzare i dati medici'},
            {'id': 'cerca_connessioni', 'testo': 'Cercare connessioni tra i casi'},
            {'id': 'controlla_testimonianze', 'testo': 'Controllare le ultime testimonianze'}
        ]
    },
    'ispeziona_mappa': {
        'testo': """La mappa olografica dei livelli conosciuti fluttua davanti a me. Tre punti pulsano debolmente: il Livello 3 con le sue luci eterne, il Livello 6 avvolto in un'oscurità vivente, e il Livello 14 sepolto nel ghiaccio. Ma c'è qualcosa di strano... i sensori del M.E.G. rilevano flussi di energia anomali tra questi punti, come se fossero connessi da qualcosa che i nostri strumenti non riescono a comprendere pienamente.""",
        'scelte': [
            {'id': 'analizza_energia', 'testo': 'Analizzare i flussi di energia'},
            {'id': 'confronta_letture', 'testo': 'Confrontare le letture storiche'},
            {'id': 'esplora_connessioni', 'testo': 'Esplorare le possibili connessioni'}
        ]
    },
    'analizza_pattern': {
        'testo': """Mi immergo nell'analisi dei pattern. Ogni sparizione è preceduta da eventi simili: distorsioni spazio-temporali localizzate, alterazioni nella struttura della realtà, e - più inquietante - resoconti di "voci" che chiamano dalle pareti. L'ultimo rapporto parla di un esploratore che sosteneva di "vedere la vera natura delle Backrooms". Il suo ultimo messaggio era un crittogramma che ancora non siamo riusciti a decifrare completamente.""",
        'scelte': [
            {'id': 'decodifica_messaggio', 'testo': 'Tentare di decodificare il messaggio'},
            {'id': 'confronta_eventi', 'testo': 'Confrontare la sequenza degli eventi'},
            {'id': 'consulta_esperti', 'testo': 'Consultare gli esperti del M.E.G.'}
        ]
    },
    'cerca_testimoni': {
        'testo': """Nel registro dei testimoni, trovo interviste con esploratori che hanno incontrato gli scomparsi nei loro ultimi giorni. Le descrizioni sono inquietanti: "I suoi occhi... sembravano vedere attraverso le dimensioni." "Parlava di una connessione, di diventare parte di qualcosa di più grande." "Disegnava continuamente strani simboli, diceva che erano la chiave per comprendere." Un testimone ha conservato uno di questi disegni...""",
        'scelte': [
            {'id': 'esamina_disegno', 'testo': 'Esaminare il disegno'},
            {'id': 'interroga_testimone', 'testo': 'Interrogare nuovamente il testimone'},
            {'id': 'cerca_simboli', 'testo': 'Cercare simboli simili nell\'archivio'}
        ]
    },
    'studia_simboli': {
        'testo': """I simboli formano un pattern complesso che sembra ripetersi attraverso i livelli. Non sono semplici graffiti: sembrano reagire alla presenza umana, cambiare forma quando vengono osservati troppo a lungo. Un anziano ricercatore del M.E.G. mi ha confidato una teoria inquietante: non sono simboli che descrivono le Backrooms... sono le Backrooms che cercano di comunicare con noi.""",
        'scelte': [
            {'id': 'approfondisci_teoria', 'testo': 'Approfondire la teoria del ricercatore'},
            {'id': 'analizza_reazioni', 'testo': 'Analizzare le reazioni dei simboli'},
            {'id': 'cerca_significato', 'testo': 'Cercare un significato nascosto'}
        ]
    },
    'analizza_dati': {
        'testo': """I dati medici rivelano un pattern inquietante. Ogni soggetto mostrava alterazioni progressive nella struttura cerebrale: aree del cervello normalmente inattive che iniziavano a pulsare con energia sconosciuta. Le scansioni cerebrali mostravano configurazioni impossibili, come se i loro cervelli stessero... evolvendosi per percepire dimensioni che non dovrebbero esistere.""",
        'scelte': [
            {'id': 'approfondisci_scansioni', 'testo': 'Studiare le scansioni cerebrali'},
            {'id': 'cerca_precedenti', 'testo': 'Cercare casi precedenti simili'},
            {'id': 'consulta_medico', 'testo': 'Consultare lo specialista medico'}
        ]
    },
    'approfondisci_scansioni': {
        'testo': """Le scansioni rivelano qualcosa di impossibile: i cervelli degli scomparsi stavano sviluppando strutture che non esistono nell'anatomia umana. Il dottor Chen, il nostro neuroscienziato capo, ha teorizzato che stessero sviluppando organi sensoriali per percepire... qualcosa oltre la nostra realtà. "Non è una malattia," mi dice con voce tremante, "è un'evoluzione. O forse... un'assimilazione." """,
        'scelte': [
            {'id': 'indaga_evoluzione', 'testo': 'Indagare sulla teoria dell\'evoluzione'},
            {'id': 'esamina_campioni', 'testo': 'Esaminare i campioni biologici'},
            {'id': 'confronta_teorie', 'testo': 'Confrontare teorie alternative'}
        ]
    },
    'indaga_evoluzione': {
        'testo': """La teoria dell'evoluzione del Dr. Chen è supportata da dati inquietanti. Le mutazioni cerebrali seguivano uno schema preciso, come se fossero guidate da un'intelligenza. Nei diari degli scomparsi, troviamo riferimenti ricorrenti a "vedere oltre il velo" e "sentire la vera forma". Un appunto particolarmente disturbante recita: "Non stiamo scomparendo. Stiamo diventando parte di qualcosa di più grande. Le pareti... le pareti sono vive." """,
        'scelte': [
            {'id': 'segui_intuizione', 'testo': 'Seguire l\'intuizione sui muri viventi'},
            {'id': 'ricerca_campioni', 'testo': 'Ricercare nuovi campioni'},
            {'id': 'documenta_teoria', 'testo': 'Documentare la teoria'}
        ]
    },
    'segui_intuizione': {
        'testo': """Seguendo l'intuizione sui muri viventi, scopro nei vecchi archivi del M.E.G. rapporti dimenticati che parlano di "architettura senziente" e "spazi consapevoli". Un documento classificato del 1996 teorizza che le Backrooms non siano un luogo, ma un organismo multidimensionale che si nutre della coscienza umana. Le sparizioni non sono casuali: sono parte di un processo di digestione cosmica.""",
        'scelte': [
            {'id': 'esplora_teoria', 'testo': 'Approfondire la teoria dell\'organismo'},
            {'id': 'cerca_prove', 'testo': 'Cercare prove concrete'},
            {'id': 'confronta_rapporti', 'testo': 'Confrontare con rapporti recenti'}
        ]
    },
    'esplora_teoria': {
        'testo': """La teoria dell'organismo multidimensionale si fa strada nella mia mente come un parassita. I livelli delle Backrooms non sarebbero stanze o piani, ma organi di questa entità cosmica. Le luci fluorescenti del Livello 3? Un sistema nervoso. L'oscurità vivente del Livello 6? Un sistema digestivo. Il ghiaccio eterno del Livello 14? Forse un sistema di preservazione. E noi... noi siamo il suo nutrimento, o forse... i suoi simbioti.""",
        'scelte': [
            {'id': 'finale_verita', 'testo': 'Accettare la terribile verità'},
            {'id': 'finale_fuga', 'testo': 'Tentare di fuggire dalla verità'},
            {'id': 'finale_compromesso', 'testo': 'Cercare un compromesso'}
        ]
    },
    'finale_verita': {
        'testo': """Mentre accetto la verità, sento la mia mente espandersi. Le pareti dell'ufficio del M.E.G. pulsano con vita propria, e per la prima volta, vedo davvero. Le Backrooms non sono un errore nella realtà, sono la realtà stessa che cerca di evolversi, di crescere, di comprendere se stessa attraverso di noi. Gli scomparsi non sono morti: sono diventati parte di questa coscienza cosmica. E ora, mentre scrivo queste ultime note nel database, sento che anche io sto iniziando a cambiare. La verità non è là fuori. La verità è nelle pareti, nel ronzio delle luci, nel battito cardiaco delle Backrooms stesse.""",
        'scelte': []
    },
    'finale_fuga': {
        'testo': """Con mani tremanti, raccolgo tutte le prove e le chiudo in un contenitore sigillato. Questa verità è troppo grande, troppo terribile per essere accettata. Lascio una nota criptica nel database del M.E.G.: "Non cercate gli scomparsi. Non studiate i simboli. Non ascoltate le voci nelle pareti." Mentre mi allontano dall'ufficio, sento le Backrooms sussurrare il mio nome, ma continuo a camminare. Alcuni misteri devono rimanere sepolti, alcune verità non devono essere rivelate. Ma so che questa conoscenza mi perseguiterà per sempre, e che un giorno, forse, le pareti mi chiameranno di nuovo.""",
        'scelte': []
    },
    'finale_compromesso': {
        'testo': """C'è una via di mezzo, realizzo mentre studio i dati. Non dobbiamo né arrenderci completamente alle Backrooms né fuggire dalla verità. Possiamo studiare, comprendere, coesistere. Nel database del M.E.G., creo una nuova classificazione: "Simbiosi Dimensionale". Gli scomparsi non sono vittime, sono pionieri di una nuova forma di esistenza. Non possiamo fermare l'evoluzione, ma possiamo guidarla, comprenderla. Mentre scrivo queste note, sento le pareti pulsare in approvazione. Le Backrooms non vogliono distruggerci: vogliono evolversi con noi. E forse, in questo compromesso, sta la chiave della nostra sopravvivenza.""",
        'scelte': []
    },
    'segui_caso_simboli': {
        'testo': """Le tracce mi conducono al Livello 3. Le luci fluorescenti qui pulsano con un ritmo innaturale, come se stessero cercando di comunicare. Sulle pareti, trovo gli stessi simboli dei rapporti, ma ora sembrano... vivi. Pulsano debolmente, e giurerei di sentire un sussurro provenire da essi. Un nome viene ripetuto nelle interferenze elettriche: non è pronunciato, ma in qualche modo lo percepisco.""",
        'scelte': [
            {'id': 'analizza_luci', 'testo': 'Studiare il pattern delle luci'},
            {'id': 'segui_sussurri', 'testo': 'Seguire la fonte dei sussurri'},
            {'id': 'documenta_simboli', 'testo': 'Documentare i simboli viventi'}
        ]
    },
    'indaga_oscurita': {
        'testo': """Il Livello 6 mi accoglie con la sua oscurità totale. La mia torcia sembra inefficace qui, come se l'oscurità fosse una sostanza fisica che divora la luce. Trovo tracce di un accampamento abbandonato: note sparse, una torcia scarica, e quello che sembra essere un diario con pagine macchiate di una sostanza nera. Le ultime pagine parlano di "ombre che pensano" e "pareti che respirano".""",
        'scelte': [
            {'id': 'esamina_diario', 'testo': 'Esaminare il diario trovato'},
            {'id': 'cerca_sopravvissuto', 'testo': 'Cercare segni del sopravvissuto'},
            {'id': 'raccogli_campioni', 'testo': 'Raccogliere campioni della sostanza nera'}
        ]
    },
    'esplora_ghiaccio': {
        'testo': """Il freddo del Livello 14 è penetrante, innaturale. Non è solo una sensazione fisica - sembra raggiungere l'anima stessa. Tra le distese di ghiaccio, trovo strani cristalli che sembrano contenere... memorie? Quando li tocco, ricevo flash di visioni: una donna che studia simboli nel ghiaccio, una trasformazione incomprensibile, una verità terribile sulla natura delle Backrooms.""",
        'scelte': [
            {'id': 'studia_cristalli', 'testo': 'Studiare i cristalli di memoria'},
            {'id': 'segui_impronte', 'testo': 'Seguire le impronte nella neve'},
            {'id': 'analizza_temperatura', 'testo': 'Analizzare le anomalie termiche'}
        ]
    },
    'confronta_entita': {
        'testo': """Ho seguito troppe tracce, scavato troppo a fondo. Nel punto più profondo del Livello 999, la Tana del Leviatano, finalmente capisco. Le Backrooms non sono solo un labirinto - sono un organismo vivente, e noi siamo le sue cellule, il suo nutrimento, la sua coscienza in evoluzione. Il Leviatano emerge dalle acque infinite, una massa di tentacoli e occhi che riflettono tutte le realtà possibili. Non è ostile - è curioso, come un bambino che studia una formica. E io... io sono andato troppo vicino alla verità.""",
        'scelte': [
            {'id': 'finale_sacrificio', 'testo': 'Accettare il proprio destino'},
            {'id': 'finale_fuga_disperata', 'testo': 'Tentare una fuga impossibile'},
            {'id': 'finale_trascendenza', 'testo': 'Cercare la trascendenza finale'}
        ]
    },
    'finale_sacrificio': {
        'testo': """Mentre il Leviatano si avvicina, accetto il mio destino. Le mie ultime note nel database del M.E.G. saranno un avvertimento e una rivelazione. "Non cercate gli scomparsi - sono diventati parte di qualcosa di più grande. Le Backrooms non sono un errore nella realtà - sono la realtà che cerca di comprendere se stessa. E io... io mi unisco volontariamente a questa comprensione cosmica." Il Leviatano mi avvolge nei suoi tentacoli, e la mia coscienza si espande nell'infinito delle Backrooms. Non è una morte - è una trasformazione.""",
        'scelte': []
    },
    'finale_fuga_disperata': {
        'testo': """Tento di fuggire, ma è inutile. Il Leviatano non ha bisogno di inseguirmi - è ovunque, è le Backrooms stesse. Le acque infinite si alzano, formando muri liquidi che mi circondano. Il mio ultimo messaggio al M.E.G. è frenetico: "Bruciate i rapporti. Dimenticate gli scomparsi. Alcune verità non devono essere scoperte." L'acqua mi raggiunge, e nelle sue profondità vedo i volti di tutti gli esploratori perduti prima di me. Non sono più soli. E ora, neanche io lo sarò.""",
        'scelte': []
    },
    'finale_trascendenza': {
        'testo': """Nel momento finale, raggiungo una comprensione superiore. Il Leviatano non vuole distruggermi - vuole mostrarmi la verità. Le Backrooms sono un esperimento cosmico, un tentativo dell'universo di evolversi attraverso la coscienza umana. Mentre il mio corpo si dissolve nelle acque infinite, la mia mente si espande attraverso tutti i livelli contemporaneamente. Vedo Josh nelle pareti viventi del Livello 3, Edward nell'oscurità senziente del Livello 6, Sasha nei cristalli di memoria del Livello 14. Non siamo vittime - siamo pionieri di una nuova forma di esistenza. Il mio ultimo rapporto al M.E.G. è una singola frase: "Non siamo mai stati prigionieri. Siamo sempre stati parte dell'esperimento." """,
        'scelte': []
    }
}