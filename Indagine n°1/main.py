import os
import time
import random
import sys
from storia import contenuto_storia
from storia_livello6 import contenuto_storia_livello6
from storia_livello14 import contenuto_storia_livello14
from storia_livello1 import contenuto_storia_livello1
from storia_livello999 import contenuto_storia_livello999
from storia_livello741 import contenuto_storia_livello741
from storia_livello013 import contenuto_storia_livello013

# File per salvare i progressi
PROGRESS_FILE = "progress.txt"

def get_unlocked_chapters():
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        # Se il file non esiste, solo il primo capitolo è sbloccato
        with open(PROGRESS_FILE, 'w') as f:
            f.write('1')
        return 1

def unlock_next_chapter():
    current = get_unlocked_chapters()
    if current < 7:  # Massimo 7 capitoli
        with open(PROGRESS_FILE, 'w') as f:
            f.write(str(current + 1))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_lento(testo, velocita=0.03):
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocita)
    print()

def caricamento():
    clear_screen()
    print("\nCaricamento", end="")
    for _ in range(random.randint(3, 6)):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

def mostra_titolo():
    clear_screen()
    logo = """
██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ███╗   ███╗███████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██╔════╝
██████╔╝███████║██║     █████╔╝ ██████╔╝██║   ██║██║   ██║██╔████╔██║███████╗
██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║╚════██║
██████╔╝██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝
"""
    print(logo)
    print("\nCapitoli disponibili:")

    unlocked = get_unlocked_chapters()
    capitoli = [
        "1. Livello 3: Le Memorie di Josh",
        "2. Livello 6: Le Memorie di Edward",
        "3. Livello 14: Le Memorie di Sasha",
        "4. Livello 1: Le Indagini di Mike (M.E.G.)",
        "5. Livello 999 - La Tana del Leviatano",
        "6. Livello 741 - La Biblioteca Infinita",
        "7. Livello 013 - La Stanza delle Opportunità Perse"
    ]

    for i, capitolo in enumerate(capitoli, 1):
        if i <= unlocked:
            print(capitolo)
        else:
            print(f"{i}. [BLOCCATO] Completa il capitolo precedente per sbloccare")

    while True:
        try:
            scelta = input("\nInserisci il numero del capitolo (1-7): ").strip()
            if scelta.isdigit():
                num = int(scelta)
                if 1 <= num <= unlocked:
                    return num
                elif 1 <= num <= 7:
                    print("Questo capitolo è bloccato. Completa prima i capitoli precedenti.")
                else:
                    print("Per favore, inserisci un numero tra 1 e 7.")
            else:
                print("Per favore, inserisci un numero valido.")
        except (KeyboardInterrupt, EOFError):
            print("\nUscita dal gioco...")
            sys.exit(0)

def mostra_storia(stato_corrente):
    clear_screen()
    print("\n" + "=" * 80)
    print_lento(stato_corrente['testo'])
    print("=" * 80 + "\n")

    if stato_corrente.get('scelte'):
        print("Cosa vuoi fare?\n")
        for i, scelta in enumerate(stato_corrente['scelte'], 1):
            print(f"{i}. {scelta['testo']}")
        return True
    return False

def get_scelta(max_scelte):
    while True:
        try:
            scelta = input("\nInserisci il numero della tua scelta: ").strip()
            if not scelta:
                print("Per favore, inserisci un numero.")
                continue
            num = int(scelta)
            if 1 <= num <= max_scelte:
                return num
            print(f"Per favore, inserisci un numero tra 1 e {max_scelte}.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")
        except (KeyboardInterrupt, EOFError):
            print("\nUscita dal gioco...")
            sys.exit(0)

def gioca(storia_selezionata, capitolo_corrente):
    stato_corrente = storia_selezionata['inizio']
    while True:
        try:
            caricamento()
            ha_scelte = mostra_storia(stato_corrente)

            if not ha_scelte:
                print_lento("\nFINE DEL CAPITOLO", velocita=0.1)
                print("\nCreato da Jashin L.")
                print("\nGrazie per aver giocato!")
                # Sblocca il prossimo capitolo quando si finisce quello corrente
                unlock_next_chapter()
                return

            scelta = get_scelta(len(stato_corrente['scelte']))
            prossimo_stato = stato_corrente['scelte'][scelta-1]['id']

            if prossimo_stato in storia_selezionata:
                stato_corrente = storia_selezionata[prossimo_stato]
            else:
                print(f"\nErrore: Stato '{prossimo_stato}' non trovato.")
                time.sleep(2)

        except (KeyboardInterrupt, EOFError):
            print("\nUscita dal gioco...")
            sys.exit(0)

def main():
    try:
        capitolo = mostra_titolo()
        if capitolo == 1:
            storia_selezionata = contenuto_storia
        elif capitolo == 2:
            storia_selezionata = contenuto_storia_livello6
        elif capitolo == 3:
            storia_selezionata = contenuto_storia_livello14
        elif capitolo == 4:
            storia_selezionata = contenuto_storia_livello1
        elif capitolo == 5:
            storia_selezionata = contenuto_storia_livello999
        elif capitolo == 6:
            storia_selezionata = contenuto_storia_livello741
        elif capitolo == 7:
            storia_selezionata = contenuto_storia_livello013
        else:
            storia_selezionata = contenuto_storia_livello013
        gioca(storia_selezionata, capitolo)
    except Exception as e:
        print(f"\nErrore imprevisto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()