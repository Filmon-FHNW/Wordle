# launch.py
import re
import time
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

VALID_WORD_RE = re.compile(r"^[A-Za-z]+$")

MIN_WORDS_TO_ENABLE = 15
MAX_WORDS = 100_000

# --- Theme colors (DarkBlue) ---
DARK_BG = "#0b1b2b"          #  (dark blue)
DARK_PANEL = "#0f2238"       #
DARK_TEXT_BG = "#0f1824"     #  (dark, slightly blue)
DARK_TEXT_FG = "#e6eefc"     # terminal/text color
DARK_BORDER = "#223a55"      # subtle border

LIGHT_BG = "#f3f6fb"
LIGHT_PANEL = "#ffffff"
LIGHT_TEXT_BG = "#ffffff"
LIGHT_TEXT_FG = "#111111"
LIGHT_BORDER = "#d0d7e2"


def is_valid_word(w: str) -> bool:
    return bool(VALID_WORD_RE.fullmatch(w))


def normalize(w: str) -> str:
    return w.strip().lower()


class WordLengthFilterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ipro Wordle WordFilter")
        self.geometry("1100x650")
        self.minsize(900, 520)

        self.dark_mode = tk.BooleanVar(value=True)
        self.length_var = tk.IntVar(value=5)

        #Speichert die letzten gültigen Wörter, damit der Nutzer sie erneut filtern kann, ohne den Text neu einzufügen
        self._cached_words = []
        self._cached_total = 0

        self._build_ui()
        self._apply_theme()

        # React to changes
        self.text.bind("<<Modified>>", self._on_text_modified)
        self.length_var.trace_add("write", lambda *_: self._update_length_label())

        # Initial UI state
        self._update_length_label()
        self._update_search_button_state()
        self._set_status("Ready")

    # ---------------- UI ----------------
    def _build_ui(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        # Font (slightly bigger)
        self.ui_font = tkfont.Font(family="Helvetica", size=16)
        self.mono_font = tkfont.Font(family="Menlo", size=16)

        #linke panel
        self.left = ttk.Frame(self, padding=14)
        self.left.grid(row=0, column=0, sticky="nsw")
        self.left.columnconfigure(0, weight=1)
        # Make a flexible spacer so Dark Mode sits at the bottom
        self.left.rowconfigure(20, weight=1)

        ttk.Label(self.left, text="Words Length 0 - 10:").grid(row=0, column=0, sticky="w", pady=(0, 6))

        # Länge wählen: Für Wordle meist 5 Buchstaben.
        # habe 1–20 eingestellt
        self.length_scale = ttk.Scale(
            self.left,
            from_=1,
            to=20,
            orient="horizontal",
            command=self._on_scale_change,
        )
        self.length_scale.set(self.length_var.get())
        self.length_scale.grid(row=1, column=0, sticky="we")

        self.length_label = ttk.Label(self.left, text="")
        self.length_label.grid(row=2, column=0, sticky="w", pady=(6, 12))

        self.search_btn = ttk.Button(self.left, text="Filter", command=self._run_filter, state="disabled")
        self.search_btn.grid(row=3, column=0, sticky="we", pady=(0, 10))

        self.rules_label = ttk.Label(
            self.left,
            text=(
                "Rules:\n\n\n"
                "• Paste more than ≥ 15 valid words\n\n\n"
                "• Max 100,000 words\n\n\n"
                "• Only A–Z letter ( Words with ö,ü,ä symbols, numbers will be ignored)\n\n\n"
                "• Click Filter to show only words\n\n\n"
                "  with the selected length"
            ),
            justify="left",
        )
        self.rules_label.grid(row=12, column=0, sticky="w", pady=(8, 0))

        # Abstand schiebt den Schalter nach unten
        ttk.Label(self.left, text="").grid(row=20, column=0, sticky="nsew")

        self.dark_toggle = ttk.Checkbutton(
            self.left,
            text="Dark Mode",
            variable=self.dark_mode,
            command=self._apply_theme,
        )
        self.dark_toggle.grid(row=21, column=0, sticky="w")

        # rechte panel (single  terminal)
        self.right = ttk.Frame(self, padding=14)
        self.right.grid(row=0, column=1, sticky="nsew")
        self.right.columnconfigure(0, weight=1)
        self.right.rowconfigure(1, weight=1)

        ttk.Label(self.right, text="Paste your word list here (space or newline separated):").grid(
            row=0, column=0, sticky="w", pady=(0, 6)
        )

        self.text = tk.Text(self.right, wrap="word", undo=True)
        self.text.grid(row=1, column=0, sticky="nsew")

        scroll = ttk.Scrollbar(self.right, orient="vertical", command=self.text.yview)
        scroll.grid(row=1, column=1, sticky="ns")
        self.text.configure(yscrollcommand=scroll.set)

        # Untere Statusleiste
        self.status = ttk.Label(self, text="", anchor="w", padding=(10, 6))
        self.status.grid(row=1, column=0, columnspan=2, sticky="we")

    # ---------------Design ----------------
    def _apply_theme(self):
        dm = self.dark_mode.get()

        bg = DARK_BG if dm else LIGHT_BG
        panel = DARK_PANEL if dm else LIGHT_PANEL
        text_bg = DARK_TEXT_BG if dm else LIGHT_TEXT_BG
        text_fg = DARK_TEXT_FG if dm else LIGHT_TEXT_FG
        border = DARK_BORDER if dm else LIGHT_BORDER

        self.configure(bg=bg)

        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=(text_fg if dm else "#111111"), font=self.ui_font)
        style.configure("TCheckbutton", background=bg, foreground=(text_fg if dm else "#111111"), font=self.ui_font)
        style.configure("TButton", padding=(10, 8), font=self.ui_font)
        style.configure("Horizontal.TScale", background=bg)

        # Macht das linke Feld wie ein Panel
        self.left.configure(style="TFrame")
        self.right.configure(style="TFrame")

        # text design
        self.text.configure(
            bg=text_bg,
            fg=text_fg,
            insertbackground=text_fg,
            highlightbackground=border,
            highlightcolor=border,
            highlightthickness=1,
            relief="flat",
            font=self.mono_font,
        )

        self.status.configure(background=bg, foreground=(text_fg if dm else "#111111"), font=self.ui_font)

    # ---------------- Logik ----------------
    def _on_scale_change(self, value):
        try:
            self.length_var.set(int(round(float(value))))
        except ValueError:
            self.length_var.set(5)

    def _update_length_label(self):
        n = self.length_var.get()
        self.length_label.configure(text=f"Showing only words with exactly {n} letters")

    def _extract_valid_words(self):
        raw = self.text.get("1.0", "end").strip()
        if not raw:
            return [], 0, 0  # worter, gültige Anzahl, Gesamtzahl der tokens

        tokens = re.split(r"\s+", raw)
        total_tokens = 0
        valid = []

        for t in tokens:
            t = t.strip()
            if not t:
                continue
            total_tokens += 1
            if is_valid_word(t):
                valid.append(normalize(t))
                if len(valid) >= MAX_WORDS:
                    # nach dem Maximum stoppen
                    break

        return valid, len(valid), total_tokens

    def _on_text_modified(self, _event=None):
        self.text.edit_modified(False)
        self._update_search_button_state()

    def _update_search_button_state(self):
        words, valid_count, _total_tokens = self._extract_valid_words()

        # gultige Wörter zwischenspeichern für schnelles Filtern
        self._cached_words = words
        self._cached_total = valid_count

        if valid_count == 0:
            self.search_btn.configure(state="disabled")
            self._set_status("Paste at least 15 valid words")
            return

        if valid_count < MIN_WORDS_TO_ENABLE:
            self.search_btn.configure(state="disabled")
            self._set_status(f"Paste at least 15 valid words (currently {valid_count})")
            return

        if valid_count >= MAX_WORDS:
            self.search_btn.configure(state="normal")
            self._set_status(f"Loaded {valid_count} valid words (max {MAX_WORDS}). Extra ignored.")
            return

        self.search_btn.configure(state="normal")
        self._set_status(f"Loaded {valid_count} valid words. Ready.")

    def _set_status(self, msg: str):
        self.status.configure(text=f"Filmon Wordle Filter V1 | {msg}")

    def _run_filter(self):
        start = time.perf_counter()

        # zwischengespeicherte Wörter nutzen (schnell, ohne neu einzufügen)
        words = self._cached_words
        total = self._cached_total

        if total < MIN_WORDS_TO_ENABLE:
            return

        target_len = self.length_var.get()
        matches = [w for w in words if len(w) == target_len]

        # nur Ergebnisse im selben Terminal anzeigen (ein sauberer Bereich)
        self.text.delete("1.0", "end")
        if not matches:
            self.text.insert("end", "No matches found.\n")
        else:
            # Eindeutig halten und sortieren
            for w in sorted(set(matches)):
                self.text.insert("end", w + "\n")

        elapsed_ms = (time.perf_counter() - start) * 1000.0
        found_count = len(set(matches))
        self._set_status(f"Found {found_count} out of {total} | Elapsed: {elapsed_ms:.0f} ms")


if __name__ == "__main__":
    app = WordLengthFilterApp()
    app.mainloop()