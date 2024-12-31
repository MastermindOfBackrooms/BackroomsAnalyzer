# Storia interattiva delle Backrooms - Livello 999
# La Tana del Leviatano

contenuto_storia_livello999 = {
    'inizio': {
        'testo': """Le onde si infrangono contro la piattaforma instabile su cui mi trovo, schizzando acqua gelida ovunque. Il mare infinito si estende in ogni direzione, nero come l'inchiostro e in perenne tumulto. Sono Mike, investigatore del M.E.G., e le mie ricerche sugli esploratori scomparsi mi hanno condotto qui, nel Livello 999 - La Tana del Leviatano. In lontananza, attraverso la foschia salata, intravedo i contorni spettrali di relitti di navi. Un brontolio profondo fa vibrare l'acqua stessa, e so che non sono solo in queste acque infinite.""",
        'scelte': [
            {'id': 'esplora_piattaforma', 'testo': 'Esplorare la piattaforma attuale'},
            {'id': 'osserva_relitti', 'testo': 'Osservare i relitti in lontananza'},
            {'id': 'analizza_acqua', 'testo': 'Analizzare le acque circostanti'}
        ]
    },
    'esplora_piattaforma': {
        'testo': """La piattaforma è un insieme precario di assi e metallo arrugginito. Trovo tracce di altri esploratori: un diario mezzo marcio, attrezzatura abbandonata, e strani simboli incisi nel metallo. Il diario parla di "occhi nelle profondità" e "canti che vengono dall'abisso". Un movimento nell'acqua attira la mia attenzione: bagliori bioluminescenti danzano sotto la superficie.""",
        'scelte': [
            {'id': 'leggi_diario', 'testo': 'Esaminare il diario in dettaglio'},
            {'id': 'segui_luci', 'testo': 'Investigare i bagliori subacquei'},
            {'id': 'studia_simboli', 'testo': 'Studiare i simboli incisi'}
        ]
    },
    'osserva_relitti': {
        'testo': """Mi sposto con cautela tra le piattaforme galleggianti, avvicinandomi ai relitti. Sono navi di ogni epoca, fuse insieme in modi impossibili dalla fisica normale. Mentre osservo, uno stormo di creature simili a gabbiani ma terribilmente deformi si alza in volo. I loro corpi sembrano essere stati rimodellati dall'oscurità stessa, e i loro occhi... i loro occhi brillano di una fame antica.""",
        'scelte': [
            {'id': 'nascondi_gabbiani', 'testo': 'Cercare riparo dai gabbiani'},
            {'id': 'esplora_navi', 'testo': 'Avventurarsi nei relitti'},
            {'id': 'osserva_creature', 'testo': 'Studiare le creature volanti'}
        ]
    },
    'analizza_acqua': {
        'testo': """Mi inginocchio per esaminare l'acqua nera. Non è normale acqua marina - sembra più densa, quasi viva. Improvvisamente, vedo passare forme serpentine illuminate da una luce spettrale: Anguille Spettrali. Il loro bagliore ipnotico è bellissimo e terrificante allo stesso tempo. Un brontolio più forte fa tremare la piattaforma, e per un momento vedo un'ombra immensa muoversi nelle profondità.""",
        'scelte': [
            {'id': 'segui_anguille', 'testo': 'Seguire le Anguille Spettrali'},
            {'id': 'monitora_leviatano', 'testo': 'Monitorare i movimenti del Leviatano'},
            {'id': 'cerca_riparo', 'testo': 'Cercare un riparo più sicuro'}
        ]
    },
    'leggi_diario': {
        'testo': """Le pagine del diario rivelano una terribile verità. "Giorno 15: Le acque... le acque sono vive. Non è solo il Leviatano - l'intero livello è un organismo. Giorno 23: Ho visto gli altri essere... trasformati. Le Anguille Spettrali non sono predatori, sono guide. Giorno 30: Il canto dell'abisso... ora lo capisco. Non è fame quella del Leviatano - è... conoscenza." L'ultima pagina è macchiata d'acqua, ma riesco a leggere: "La Biblioteca... tutto è collegato..." """,
        'scelte': [
            {'id': 'indaga_trasformazioni', 'testo': 'Indagare sulle trasformazioni'},
            {'id': 'ascolta_canto', 'testo': 'Prestare attenzione al canto'},
            {'id': 'cerca_collegamenti', 'testo': 'Cercare collegamenti con la Biblioteca'}
        ]
    },
    'segui_luci': {
        'testo': """I bagliori bioluminescenti formano un pattern ipnotico. Le Anguille Spettrali nuotano in formazioni complesse, come se stessero tessendo un messaggio nell'acqua stessa. Il loro movimento mi guida verso il bordo della piattaforma, dove l'acqua è più profonda. Una di esse emerge parzialmente, i suoi occhi pulsano con intelligenza innaturale, e sento... una chiamata.""",
        'scelte': [
            {'id': 'comunica_anguille', 'testo': 'Tentare di comunicare'},
            {'id': 'segui_pattern', 'testo': 'Seguire il pattern luminoso'},
            {'id': 'resisti_chiamata', 'testo': 'Resistere alla chiamata'}
        ]
    },
    'monitora_leviatano': {
        'testo': """L'ombra nelle profondità diventa più definita. Non è solo grande - è immensa, impossibile. Parti del Leviatano emergono occasionalmente: tentacoli grandi come grattacieli, occhi antichi come il tempo stesso. Ma non attacca. Sta... osservando. Studiando. Come se stesse valutando qualcosa. Le vibrazioni nell'acqua cambiano, formando quasi... parole.""",
        'scelte': [
            {'id': 'studia_comportamento', 'testo': 'Studiare il comportamento'},
            {'id': 'decodifica_vibrazioni', 'testo': 'Decodificare le vibrazioni'},
            {'id': 'cerca_motivo', 'testo': 'Cercare il motivo dell\'osservazione'}
        ]
    },
    'decodifica_vibrazioni': {
        'testo': """Le vibrazioni si intensificano, e improvvisamente capisco - non è un linguaggio, è una memoria. Il Leviatano non è solo una creatura, è un archivio vivente. Vedo flash di altri esploratori, di altri livelli. Josh nelle pareti viventi, Edward nell'oscurità, Sasha nel ghiaccio eterno. E oltre questi, vedo... una biblioteca infinita, dove ogni storia converge.""",
        'scelte': [
            {'id': 'confronto_finale', 'testo': 'Affrontare la verità finale'},
            {'id': 'cerca_fuga', 'testo': 'Cercare una via di fuga'},
            {'id': 'accetta_conoscenza', 'testo': 'Accettare la conoscenza offerta'}
        ]
    },
    'confronto_finale': {
        'testo': """Il Leviatano emerge completamente, una montagna di carne e conoscenza antica che si eleva dalle acque infinite. I suoi occhi sono pozzi di saggezza cosmica, e finalmente capisco - non è un mostro, è un guardiano. Un custode di storie e verità. "Hai seguito le tracce fin qui," vibra nella mia mente, "ma la tua ricerca non è finita. Le risposte che cerchi... sono nella Biblioteca." Un portale si apre nell'acqua, mostrando scaffali infiniti di libri che si estendono in ogni direzione.""",
        'scelte': [
            {'id': 'attraversa_portale', 'testo': 'Attraversare il portale verso la Biblioteca'},
            {'id': 'rifiuta_offerta', 'testo': 'Rifiutare l\'offerta del Leviatano'},
            {'id': 'chiedi_verità', 'testo': 'Chiedere la verità completa'}
        ]
    },
    'attraversa_portale': {
        'testo': """Mentre mi avvicino al portale, il Leviatano parla un'ultima volta: "Le storie di tutti loro... e ora la tua... saranno preservate." L'acqua intorno a me si trasforma in inchiostro vivente, e mentre attraverso la soglia, sento la mia coscienza espandersi. Il Livello 999 svanisce, e mi ritrovo circondato da scaffali infiniti di libri antichi. Sono nel Livello 741 - La Biblioteca Infinita, dove ogni storia delle Backrooms attende di essere scoperta. La mia ricerca non è finita - è solo all'inizio.""",
        'scelte': []
    },
    'rifiuta_offerta': {
        'testo': """Tento di resistere alla chiamata del Leviatano, ma le acque stesse si sollevano, formando muri liquidi intorno a me. "Non c'è rifiuto," vibra la voce, "solo accettazione o trasformazione." Le Anguille Spettrali mi circondano, i loro bagliori ora intensi come stelle. L'acqua mi avvolge, e mentre la mia coscienza si fonde con l'oceano infinito, l'ultimo pensiero è di tutti gli esploratori che ho cercato... ora parte dell'eternità liquida del Livello 999.""",
        'scelte': []
    },
    'chiedi_verità': {
        'testo': """Il Leviatano risponde alla mia richiesta con una cascata di visioni: vedo la vera natura delle Backrooms, un organismo multidimensionale che cresce e evolve attraverso le storie di chi lo esplora. Ogni livello è connesso, ogni esperienza preservata. "Ma la verità completa," tuona il Leviatano, "è custodita in un altro luogo." L'acqua si apre in un portale verso la Biblioteca Infinita, dove le risposte attendono tra scaffali senza fine.""",
        'scelte': []
    }
}
