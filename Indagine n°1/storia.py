# Storia interattiva delle Backrooms - Livello 3
# Le memorie di Josh

contenuto_storia = {
    'inizio': {
        'testo': """Le luci fluorescenti sopra di me sfarfallano incessantemente. Vagabondo in questi corridoi da quello che sembrano giorni, ma il tempo ha perso ogni significato qui nel Livello 3. La moquette sotto i miei piedi è umida, e la carta da parati si stacca rivelando un cemento che non dovrebbe essere lì. Mi chiamo Josh, e devo trovare una via d'uscita.""",
        'scelte': [
            {'id': 'esplora_ufficio', 'testo': "Investigare l'ufficio abbandonato davanti a me"},
            {'id': 'segui_suono', 'testo': 'Seguire il ronzio distante'},
            {'id': 'ispeziona_muri', 'testo': 'Ispezionare le pareti che si stanno deteriorando'}
        ]
    },
    'ispeziona_muri': {
        'testo': """Mi avvicino alla parete. La carta si stacca facilmente sotto le mie dita, rivelando uno strano motivo nel cemento sottostante. Sembrano... volti? No, impossibile. Eppure più guardo, più mi sembra di vedere espressioni di sofferenza impresse nella pietra.""",
        'scelte': [
            {'id': 'tocca_muro', 'testo': 'Toccare i volti nel muro'},
            {'id': 'cerca_strumenti', 'testo': 'Cercare strumenti per rompere il muro'},
            {'id': 'allontanati', 'testo': 'Allontanarsi velocemente'}
        ]
    },
    'tocca_muro': {
        'testo': """Le mie dita sfiorano il cemento. È... caldo. E sta pulsando. Un sussurro risuona nella mia mente: "Unisciti a noi, Josh. Diventa parte delle pareti. È l'unico modo per sfuggire al dolore." """,
        'scelte': [
            {'id': 'resisti_voci', 'testo': 'Resistere alle voci'},
            {'id': 'ascolta_voci', 'testo': 'Ascoltare le voci'}
        ]
    },
    'cerca_strumenti': {
        'testo': """Trovo un vecchio estintore arrugginito. Potrebbe funzionare per rompere il muro. Ma mentre lo sollevo, noto che le pareti sembrano reagire, contraendosi come se fossero vive.""",
        'scelte': [
            {'id': 'colpisci_muro', 'testo': 'Colpire il muro con l\'estintore'},
            {'id': 'usa_estintore', 'testo': 'Usare l\'estintore normalmente sulle pareti'},
            {'id': 'abbandona_idea', 'testo': 'Abbandonare l\'idea e proseguire'}
        ]
    },
    'colpisci_muro': {
        'testo': """Il primo colpo risuona con un'eco innaturale. Il secondo rivela uno spazio vuoto. Il terzo... il muro urla. Un vero urlo umano. Dal buco che ho creato inizia a colare un liquido nero.""",
        'scelte': [
            {'id': 'continua_rompere', 'testo': 'Continuare a rompere il muro'},
            {'id': 'scappa_veloce', 'testo': 'Scappare il più velocemente possibile'}
        ]
    },
    'continua_rompere': {
        'testo': """Ogni colpo allarga il buco, ma il liquido nero aumenta. Improvvisamente, una mano emerge dal buco, afferrandomi il polso. È fredda e viscida.""",
        'scelte': [
            {'id': 'liberati', 'testo': 'Cercare di liberarti'},
            {'id': 'attacca_mano', 'testo': 'Colpire la mano con l\'estintore'}
        ]
    },
    'liberati': {
        'testo': """Mi dimeno con tutte le mie forze, ma la presa è troppo forte. Altri arti emergono dal buco, cercando di trascinarmi dentro. La parete stessa sembra animarsi.""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Lottare fino alla fine'},
            {'id': 'finale_assorbimento', 'testo': 'Arrendersi all\'inevitabile'}
        ]
    },
    'attacca_mano': {
        'testo': """L'estintore colpisce con un suono sordo. La mano mi lascia andare, ma il liquido nero inizia a ribollire violentemente. Dal buco emergono suoni... risate?""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Affrontare qualunque cosa stia emergendo'},
            {'id': 'finale_assorbimento', 'testo': 'Tentare una fuga disperata'}
        ]
    },
    'scappa_veloce': {
        'testo': """Mi volto per correre, ma il pavimento sotto di me ha iniziato a mutare. La moquette si è trasformata in una sostanza simile a melma che rallenta i miei movimenti.""",
        'scelte': [
            {'id': 'salta_mobili', 'testo': 'Saltare sui mobili per evitare il pavimento'},
            {'id': 'continua_correre', 'testo': 'Continuare a correre ignorando la melma'}
        ]
    },
    'esplora_ufficio': {
        'testo': """Lo spazio dell'ufficio si estende davanti a me, un labirinto infinito di cubicoli. Documenti di decenni passati ricoprono il pavimento, e antichi computer sono ricoperti di polvere. Qualcosa si muove nella mia visione periferica. Un brivido mi percorre la schiena mentre cerco di capire cosa fare.""",
        'scelte': [
            {'id': 'nascondi_scrivania', 'testo': 'Nascondersi sotto una scrivania'},
            {'id': 'investiga_movimento', 'testo': 'Voltarsi per affrontare qualunque cosa si sia mossa'},
            {'id': 'cerca_uscita', 'testo': 'Cercare silenziosamente una via di fuga'}
        ]
    },
    'cerca_uscita': {
        'testo': """Mi muovo silenziosamente tra i cubicoli, cercando una via di fuga. In lontananza vedo il bagliore di un'insegna di uscita, ma qualcosa nel modo in cui la luce si riflette non sembra giusto.""",
        'scelte': [
            {'id': 'segui_insegna', 'testo': 'Seguire l\'insegna di uscita'},
            {'id': 'cerca_altra_via', 'testo': 'Cercare un\'altra via di fuga'},
            {'id': 'nascondi_documenti', 'testo': 'Nascondersi tra i documenti'}
        ]
    },
    'segui_insegna': {
        'testo': """Mi avvicino all'insegna. La luce rossa sembra pulsare con un ritmo quasi ipnotico. Mentre mi avvicino, noto che le lettere stanno... cambiando? Non dicono più "USCITA" ma qualcos'altro...""",
        'scelte': [
            {'id': 'leggi_insegna', 'testo': 'Cercare di leggere cosa dice l\'insegna'},
            {'id': 'ignora_testo', 'testo': 'Ignorare il testo e proseguire'},
            {'id': 'torna_indietro', 'testo': 'Tornare indietro finché si è in tempo'}
        ]
    },
    'leggi_insegna': {
        'testo': """Mi sforzo di leggere le lettere che continuano a mutare. "NESSUNA USCITA", "RESTA CON NOI", "DIVENTA UNO"... ogni frase più inquietante della precedente. La luce rossa inizia a espandersi, avvolgendo tutto.""",
        'scelte': [
            {'id': 'chiudi_occhi', 'testo': 'Chiudere gli occhi e correre via'},
            {'id': 'affronta_luce', 'testo': 'Affrontare qualunque cosa si nasconda nella luce'}
        ]
    },
    'segui_suono': {
        'testo': """Il ronzio diventa più forte mentre avanzo. Non è meccanico - è quasi... organico. Il corridoio sembra pulsare con ogni onda sonora. Le pareti vibrano in modo innaturale, e l'aria diventa più densa ad ogni passo.""",
        'scelte': [
            {'id': 'continua_avanti', 'testo': 'Proseguire verso la fonte del suono'},
            {'id': 'torna_indietro', 'testo': 'Tornare indietro finché si è in tempo'},
            {'id': 'esplora_stanze', 'testo': 'Esplorare le stanze laterali'}
        ]
    },
    'esplora_stanze': {
        'testo': """Apro una delle porte laterali. La stanza è piena di vecchie apparecchiature mediche. Un monitor cardiaco in un angolo sta ancora funzionando, il suo bip regolare si mescola al ronzio. Sul pavimento, tracce di quello che sembra sangue secco formano strani simboli.""",
        'scelte': [
            {'id': 'esamina_simboli', 'testo': 'Esaminare i simboli sul pavimento'},
            {'id': 'controlla_monitor', 'testo': 'Controllare il monitor cardiaco'},
            {'id': 'cerca_medicinali', 'testo': 'Cercare medicinali utili'}
        ]
    },
    'esamina_simboli': {
        'testo': """Mi chino per osservare meglio i simboli. Sembrano... pulsare? No, è il pavimento stesso che sta pulsando. I simboli iniziano a brillare di una tenue luce rossastra, e posso sentire un calore emanare da essi.""",
        'scelte': [
            {'id': 'tocca_simboli', 'testo': 'Toccare i simboli luminosi'},
            {'id': 'copia_simboli', 'testo': 'Provare a copiare i simboli'},
            {'id': 'lascia_stanza', 'testo': 'Lasciare immediatamente la stanza'}
        ]
    },
    'tocca_simboli': {
        'testo': """Nel momento in cui le mie dita toccano i simboli, una scarica di energia attraversa il mio corpo. Visioni di altri livelli delle Backrooms invadono la mia mente. Vedo... altre persone? No, non sono più persone...""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Cercare di resistere alle visioni'},
            {'id': 'finale_assorbimento', 'testo': 'Lasciarsi trasportare dalle visioni'}
        ]
    },
    'finale_assorbimento': {
        'testo': """Le luci fluorescenti sopra di me esplodono in una cascata di scintille. Nell'oscurità, finalmente capisco. Non ero mai destinato a fuggire. Le Backrooms non lasciano andare ciò che gli appartiene. Mentre la coscienza svanisce, divento un tutt'uno con il Livello 3, un'altra storia per i futuri vagabondi da scoprire. Le pareti pulsano con il ritmo del mio cuore, che ora batte all'unisono con l'edificio stesso. Sono casa. Sono il Livello 3.""",
        'scelte': []
    },
    'nascondi_scrivania': {
        'testo': """Mi rannicchio sotto la scrivania, il cuore che batte all'impazzata. Dei passi si avvicinano - suonano sbagliati, troppi arti che si muovono con un ritmo innaturale. Il suono dei passi rallenta, come se qualcosa stesse... annusando l'aria.""",
        'scelte': [
            {'id': 'resta_immobile', 'testo': 'Trattenere il respiro e restare immobile'},
            {'id': 'corri', 'testo': 'Tentare una fuga disperata'}
        ]
    },
    'investiga_movimento': {
        'testo': """Mi volto di scatto per affrontare il movimento. La figura è incredibilmente alta, le sue proporzioni sono tutte sbagliate. Ha troppi arti, troppi angoli acuti dove dovrebbero esserci curve morbide. Mi vede, e qualcosa che potrebbe essere un sorriso si apre sul suo volto - se di volto si può parlare.""",
        'scelte': [
            {'id': 'parla', 'testo': 'Tentare di comunicare con la creatura'},
            {'id': 'attacca', 'testo': 'Attaccare per primo, sperando in un elemento sorpresa'}
        ]
    },
    'continua_avanti': {
        'testo': """Il ronzio si trasforma in un coro di voci impossibili. Le pareti pulsano con una luce giallastra malata. Qualcosa mi aspetta dietro l'angolo, posso sentire la sua presenza che preme contro la mia mente.""",
        'scelte': [
            {'id': 'affronta_presenza', 'testo': 'Affrontare qualunque cosa mi stia aspettando'},
            {'id': 'cerca_altra_via', 'testo': "Cercare disperatamente un'altra via"}
        ]
    },
    'torna_indietro': {
        'testo': """Mi volto per fuggire, ma il corridoio dietro di me è cambiato. Le pareti respirano ora, si espandono e contraggono come polmoni malati. Non c'è più via del ritorno.""",
        'scelte': [
            {'id': 'accetta_destino', 'testo': 'Accettare il proprio destino'},
            {'id': 'combatti', 'testo': "Lottare contro l'inevitabile"}
        ]
    },
    'resta_immobile': {
        'testo': """Il mio cuore batte così forte che sono sicuro possa sentirlo. I passi si fermano proprio davanti alla scrivania. Un liquido viscoso gocciola dal bordo del tavolo. Non oso guardare in alto.""",
        'scelte': [
            {'id': 'guarda_su', 'testo': 'Alzare lentamente lo sguardo'},
            {'id': 'chiudi_occhi', 'testo': 'Chiudere gli occhi e pregare'}
        ]
    },
    'corri': {
        'testo': """Scatto in piedi e comincio a correre. Il rumore dietro di me è un misto tra uno stridio metallico e un ringhio animale. Il pavimento sotto i miei piedi inizia a cedere, come se stesse sciogliendosi.""",
        'scelte': [
            {'id': 'salta_finestra', 'testo': 'Tentare di saltare attraverso una finestra'},
            {'id': 'continua_correre', 'testo': 'Continuare a correre ignorando il pavimento che cede'}
        ]
    },
    'parla': {
        'testo': """"Aspetta!" grido, alzando le mani in segno di resa. La creatura inclina quello che dovrebbe essere il suo capo. Un suono come statica radio riempie la mia mente.""",
        'scelte': [
            {'id': 'ascolta', 'testo': 'Concentrarsi sulla statica, cercando di capire'},
            {'id': 'scappa', 'testo': 'Approfittare del momento per fuggire'}
        ]
    },
    'attacca': {
        'testo': """Mi lancio contro la creatura, cercando di colpirla. È come colpire nebbia solida. Le mie mani attraversano la sua forma, ma qualcosa di freddo e viscido si aggrappa alla mia pelle.""",
        'scelte': [
            {'id': 'strappa', 'testo': 'Cercare di strapparsi via quella sostanza'},
            {'id': 'accetta', 'testo': "Accettare l'inevitabile trasformazione"}
        ]
    },
    'affronta_presenza': {
        'testo': """Volto l'angolo. La realtà stessa sembra piegarsi e contorcersi. Una figura impossibile fluttua nel centro della stanza, circondata da quello che sembra essere tempo cristallizzato.""",
        'scelte': [
            {'id': 'raggiungila', 'testo': 'Avanzare verso la figura'},
            {'id': 'osserva', 'testo': 'Osservare, cercando di comprendere'}
        ]
    },
    'cerca_altra_via': {
        'testo': """Mi guardo intorno freneticamente, cercando un'altra via di fuga. Le pareti sembrano sussurrare, mostrandomi glimpse di altri luoghi, altri tempi, altre possibilità.""",
        'scelte': [
            {'id': 'attraversa', 'testo': 'Tentare di attraversare una delle visioni'},
            {'id': 'resisti', 'testo': 'Resistere alle visioni ingannevoli'}
        ]
    },
    'accetta_destino': {
        'testo': """Chiudo gli occhi e smetto di lottare. Le pareti si avvicinano, il respiro del corridoio diventa il mio respiro. Comincio a capire.""",
        'scelte': [
            {'id': 'finale', 'testo': 'Lasciati assorbire dal Livello 3'},
            {'id': 'ultimo_tentativo', 'testo': 'Un ultimo, disperato tentativo di resistere'}
        ]
    },
    'combatti': {
        'testo': """Mi volto e comincio a colpire le pareti pulsanti. La superficie cede sotto i miei pugni, rivelando uno strato di qualcosa che sembra carne viva.""",
        'scelte': [
            {'id': 'continua_scavare', 'testo': 'Continuare a scavare più a fondo'},
            {'id': 'finale', 'testo': 'Realizzare l\'errore fatale'}
        ]
    },
    'finale': {
        'testo': """Le luci fluorescenti sopra di me esplodono in una cascata di scintille. Nell'oscurità, finalmente capisco. Non ero mai destinato a fuggire. Le Backrooms non lasciano andare ciò che gli appartiene. Mentre la coscienza svanisce, divento un tutt'uno con il Livello 3, un'altra storia per i futuri vagabondi da scoprire.""",
        'scelte': []
    },
    'allontanati': {
        'testo': """Mi allontano velocemente dal muro. Il mio cuore batte forte nel petto. Avevo ragione, c'era qualcosa di sbagliato nelle pareti. Non oso immaginare cosa sarebbe successo se avessi continuato ad ispezionarle.""",
        'scelte': [
            {'id': 'esplora_ufficio', 'testo': 'Esplorare l\'ufficio abbandonato'},
            {'id': 'segui_suono', 'testo': 'Seguire il ronzio distante'}
        ]
    },
    'resisti_voci': {
        'testo': """Mi allontano dal muro, rifiutando di ascoltare le voci. Il calore si attenua, ma non posso scacciare l'immagine di quei volti incisi nella pietra.""",
        'scelte': [
            {'id': 'cerca_strumenti', 'testo': 'Cercare strumenti per rompere il muro'},
            {'id': 'allontanati', 'testo': 'Allontanarsi velocemente'}
        ]
    },
    'ascolta_voci': {
        'testo': """Le voci diventano più chiare, più persuasive. Mi invitano ad unirmi a loro, a diventare uno con le pareti. La promessa di un sollievo dal dolore mi seduce.""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Accettare l\'invito delle voci'},
            {'id': 'resisti_voci', 'testo': 'Resistere all\'ultimo minuto'}
        ]
    },
    'usa_estintore': {
        'testo': """Utilizzo l'estintore sulle pareti, ma non succede nulla. L'estintore è vuoto. Le pareti continuano ad osservare.""",
        'scelte': [
            {'id': 'colpisci_muro', 'testo': 'Colpire il muro con l\'estintore'},
            {'id': 'abbandona_idea', 'testo': 'Abbandonare l\'idea e proseguire'}
        ]
    },
    'abbandona_idea': {
        'testo': """Decido di proseguire, lasciando il muro intatto. C'è qualcosa di profondamente sbagliato in quel muro.""",
        'scelte': [
            {'id': 'esplora_ufficio', 'testo': 'Esplorare l\'ufficio abbandonato'},
            {'id': 'segui_suono', 'testo': 'Seguire il ronzio distante'}
        ]
    },
    'nascondi_documenti': {
        'testo': """Mi nascondo tra i documenti, sperando di non essere visto. Sento dei passi avvicinarsi.""",
        'scelte': [
            {'id': 'resta_nascosto', 'testo': 'Restar nascosto finché non se ne vanno'},
            {'id': 'cerca_altra_via', 'testo': 'Cercare un\'altra via di fuga'}
        ]
    },
    'resta_nascosto': {
        'testo': """I passi si avvicinano e poi si allontanano. Sembra che abbiano annusato l'aria e non abbiano trovato nulla. Sono al sicuro, per ora.""",
        'scelte': [
            {'id': 'cerca_uscita', 'testo': 'Cercare un\'altra via di fuga'},
            {'id': 'esplora_ufficio', 'testo': 'Esplorare il resto dell\'ufficio'}
        ]
    },
    'ignora_testo': {
        'testo': """Ignoro il testo e proseguo verso la luce. La luce rossa mi avvolge e sento un forte ronzio nelle orecchie.""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Respingere la luce'},
            {'id': 'finale_assorbimento', 'testo': 'Lasciarsi avvolgere dalla luce'}
        ]
    },
    'chiudi_occhi': {
        'testo': """Chiudo gli occhi e corro via dalla luce rossa. Sento ancora il suo calore sulla mia pelle.""",
        'scelte': [
            {'id': 'cerca_altra_via', 'testo': 'Cercare un\'altra via di fuga'},
            {'id': 'esplora_ufficio', 'testo': 'Esplorare l\'ufficio abbandonato'}
        ]
    },
    'affronta_luce': {
        'testo': """Affronto la luce rossa. Tutto si fa bianco, e poi...""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'La luce mi avvolge'}
        ]
    },
    'esplora_stanze': {
        'testo': """Apro una delle porte laterali. La stanza è piena di vecchie apparecchiature mediche. Un monitor cardiaco in un angolo sta ancora funzionando, il suo bip regolare si mescola al ronzio. Sul pavimento, tracce di quello che sembra sangue secco formano strani simboli.""",
        'scelte': [
            {'id': 'esamina_simboli', 'testo': 'Esaminare i simboli sul pavimento'},
            {'id': 'controlla_monitor', 'testo': 'Controllare il monitor cardiaco'},
            {'id': 'cerca_medicinali', 'testo': 'Cercare medicinali utili'}
        ]
    },
    'controlla_monitor': {
        'testo': """Il monitor cardiaco mostra un ritmo cardiaco irregolare, troppo veloce. Sembra che qualcuno sia stato qui poco tempo fa, e che non stia bene.""",
        'scelte': [
            {'id': 'esamina_simboli', 'testo': 'Esaminare i simboli sul pavimento'},
            {'id': 'cerca_medicinali', 'testo': 'Cercare medicinali utili'}
        ]
    },
    'cerca_medicinali': {
        'testo': """Cerco medicinali ma non trovo nulla. Solo vecchie attrezzature mediche abbandonate. Questa stanza è stata abbandonata da tempo.""",
        'scelte': [
            {'id': 'esamina_simboli', 'testo': 'Esaminare i simboli sul pavimento'},
            {'id': 'controlla_monitor', 'testo': 'Controllare il monitor cardiaco'}
        ]
    },
    'copia_simboli': {
        'testo': """Cerco di copiare i simboli, ma non riesco a ricordare come erano. La mia mente sembra annebbiata.""",
        'scelte': [
            {'id': 'tocca_simboli', 'testo': 'Toccare i simboli luminosi'},
            {'id': 'lascia_stanza', 'testo': 'Lasciare immediatamente la stanza'}
        ]
    },
    'lascia_stanza': {
        'testo': """Lascio immediatamente la stanza, il cuore che batte forte nel petto. Quella stanza mi ha dato una brutta sensazione.""",
        'scelte': [
            {'id': 'segui_suono', 'testo': 'Seguire il ronzio distante'},
            {'id': 'torna_indietro', 'testo': 'Tornare indietro'}
        ]
    },
    'salta_mobili': {
        'testo': """Cerco di saltare sui mobili per evitare la melma, ma non è facile. La melma sembra sempre più densa e appiccicosa.""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Continuare a saltare'},
            {'id': 'finale_assorbimento', 'testo': 'Arrendersi alla melma'}
        ]
    },
    'continua_correre': {
        'testo': """Continuo a correre, ma il pavimento è troppo instabile. Cedo alla melma.""",
        'scelte': [
            {'id': 'finale_assorbimento', 'testo': 'Arrendersi alla melma'}
        ]
    },
    'ultimo_tentativo': {
        'testo': """Lotta contro l'inevitabile assorbimento. Ma è inutile. Le Backrooms ti reclama.""",
        'scelte': [{'id': 'finale', 'testo': 'Arrendersi all\'inevitabile'}]
    }
}