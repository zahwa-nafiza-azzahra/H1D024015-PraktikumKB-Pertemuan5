import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# KNOWLEDGE BASE
# ============================================================

GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara / menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual / muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

PENYAKIT = {
    "Tonsilitis":                   ["G37","G12","G5","G27","G6","G21"],
    "Sinusitis Maksilaris":         ["G37","G12","G27","G17","G33","G36","G29"],
    "Sinusitis Frontalis":          ["G37","G12","G27","G17","G33","G36","G21","G26"],
    "Sinusitis Etmoidalis":         ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
    "Sinusitis Sfenoidalis":        ["G37","G12","G27","G17","G33","G36","G29","G7"],
    "Abses Peritonsiler":           ["G37","G12","G6","G15","G2","G29","G10"],
    "Faringitis":                   ["G37","G5","G6","G7","G15"],
    "Kanker Laring":                ["G5","G27","G6","G15","G2","G19","G1"],
    "Deviasi Septum":               ["G37","G17","G20","G8","G18","G25"],
    "Laringitis":                   ["G37","G5","G15","G16","G32"],
    "Kanker Leher & Kepala":        ["G5","G22","G8","G28","G3","G11"],
    "Otitis Media Akut":            ["G37","G20","G35","G31"],
    "Contact Ulcers":               ["G5","G2"],
    "Abses Parafaringeal":          ["G5","G16"],
    "Barotitis Media":              ["G12","G20"],
    "Kanker Nasofaring":            ["G17","G8"],
    "Kanker Tonsil":                ["G6","G29"],
    "Neuronitis Vestibularis":      ["G35","G24"],
    "Meniere":                      ["G20","G35","G14","G4"],
    "Tumor Saraf Pendengaran":      ["G12","G34","G23"],
    "Kanker Leher Metastatik":      ["G29"],
    "Otosklerosis":                 ["G34","G9"],
    "Vertigo Postural":             ["G24"],
}

DESKRIPSI_PENYAKIT = {
    "Tonsilitis": "Peradangan pada amandel (tonsil) yang biasanya disebabkan oleh infeksi bakteri atau virus.",
    "Sinusitis Maksilaris": "Peradangan sinus maksilaris (di area pipi) akibat infeksi atau alergi.",
    "Sinusitis Frontalis": "Peradangan sinus frontalis yang terletak di dahi, sering disertai nyeri dahi.",
    "Sinusitis Etmoidalis": "Peradangan sinus etmoidalis yang terletak di antara mata, dapat menyebabkan nyeri di area tersebut.",
    "Sinusitis Sfenoidalis": "Peradangan sinus sfenoidalis yang terletak di bagian belakang rongga hidung.",
    "Abses Peritonsiler": "Kumpulan nanah di sekitar amandel akibat infeksi bakteri yang tidak tertangani.",
    "Faringitis": "Peradangan pada faring (tenggorokan) yang menyebabkan nyeri dan sulit menelan.",
    "Kanker Laring": "Tumor ganas yang tumbuh pada laring (kotak suara), sering ditandai suara serak dan sesak napas.",
    "Deviasi Septum": "Kondisi di mana sekat hidung bergeser dari posisi normal, menyebabkan sumbatan hidung.",
    "Laringitis": "Peradangan pada laring yang menyebabkan suara serak atau hilang.",
    "Kanker Leher & Kepala": "Tumor ganas yang tumbuh di area leher dan kepala, meliputi berbagai organ.",
    "Otitis Media Akut": "Infeksi akut pada telinga tengah yang umumnya ditandai nyeri telinga dan demam.",
    "Contact Ulcers": "Luka pada pita suara akibat trauma atau refluks asam lambung.",
    "Abses Parafaringeal": "Kumpulan nanah di jaringan parafaringeal yang dapat mengancam jiwa.",
    "Barotitis Media": "Gangguan telinga akibat perubahan tekanan udara yang cepat.",
    "Kanker Nasofaring": "Tumor ganas yang tumbuh di nasofaring (belakang hidung).",
    "Kanker Tonsil": "Tumor ganas pada amandel, bagian dari kanker orofaring.",
    "Neuronitis Vestibularis": "Peradangan saraf vestibular yang menyebabkan vertigo dan mual.",
    "Meniere": "Gangguan telinga dalam yang menyebabkan vertigo episodik, tinnitus, dan gangguan pendengaran.",
    "Tumor Saraf Pendengaran": "Tumor jinak pada saraf vestibulokoklear yang menghubungkan telinga ke otak.",
    "Kanker Leher Metastatik": "Kanker yang telah menyebar ke kelenjar getah bening di leher dari sumber primer lain.",
    "Otosklerosis": "Pertumbuhan tulang abnormal di telinga tengah yang menyebabkan gangguan pendengaran progresif.",
    "Vertigo Postural": "Sensasi pusing yang dipicu oleh perubahan posisi kepala.",
}

SARAN_PENYAKIT = {
    "Tonsilitis": "Konsultasikan ke dokter THT. Pengobatan meliputi antibiotik dan pereda nyeri. Jika sering kambuh, tonsilektomi mungkin direkomendasikan.",
    "Sinusitis Maksilaris": "Gunakan dekongestan, antibiotik jika infeksi bakteri, dan cuci hidung dengan larutan saline. Hindari pemicu alergi.",
    "Sinusitis Frontalis": "Segera konsultasi dokter. Kompres hangat pada dahi, gunakan obat dekongestan dan antiradang.",
    "Sinusitis Etmoidalis": "Perlu pemeriksaan CT-scan. Pengobatan dengan antibiotik dan kortikosteroid nasal spray.",
    "Sinusitis Sfenoidalis": "Segera ke dokter spesialis THT. Terapi antibiotik dan kemungkinan tindakan bedah jika tidak membaik.",
    "Abses Peritonsiler": "Segera ke IGD/dokter THT. Memerlukan drainase abses dan antibiotik intravena.",
    "Faringitis": "Istirahat, minum air hangat, berkumur air garam hangat. Konsultasi dokter untuk kemungkinan antibiotik.",
    "Kanker Laring": "Segera rujuk ke onkologi. Pengobatan meliputi radioterapi, kemoterapi, dan/atau pembedahan.",
    "Deviasi Septum": "Konsultasi dokter THT. Tindakan septoplasti (operasi) mungkin diperlukan untuk kasus berat.",
    "Laringitis": "Istirahatkan suara, minum banyak cairan, hindari rokok dan alkohol. Konsultasi dokter jika lebih dari 2 minggu.",
    "Kanker Leher & Kepala": "Segera ke spesialis onkologi THT. Pemeriksaan biopsi dan pencitraan diperlukan.",
    "Otitis Media Akut": "Konsultasi dokter untuk antibiotik. Berikan pereda nyeri dan pastikan tidak ada komplikasi.",
    "Contact Ulcers": "Istirahatkan suara, terapi wicara, dan obati refluks asam jika ada.",
    "Abses Parafaringeal": "Kondisi darurat! Segera ke IGD. Memerlukan drainase bedah dan antibiotik IV.",
    "Barotitis Media": "Lakukan manuver Valsalva, gunakan dekongestan. Konsultasi dokter jika nyeri berlanjut.",
    "Kanker Nasofaring": "Segera ke dokter spesialis. Radioterapi merupakan pengobatan utama.",
    "Kanker Tonsil": "Rujuk ke spesialis onkologi THT untuk biopsi dan penanganan komprehensif.",
    "Neuronitis Vestibularis": "Istirahat, obat anti-vertigo (betahistin), dan fisioterapi vestibular.",
    "Meniere": "Konsultasi dokter THT. Diet rendah garam, obat diuretik, dan terapi vestibular.",
    "Tumor Saraf Pendengaran": "Segera ke dokter spesialis saraf dan THT. MRI diperlukan untuk konfirmasi diagnosis.",
    "Kanker Leher Metastatik": "Segera ke onkologi. Pencarian sumber primer kanker sangat penting.",
    "Otosklerosis": "Konsultasi dokter THT. Penggunaan alat bantu dengar atau operasi stapedektomi.",
    "Vertigo Postural": "Lakukan manuver Epley. Konsultasi dokter jika vertigo parah atau mengganggu aktivitas.",
}

# Susun pertanyaan untuk setiap kode gejala
PERTANYAAN = {kode: f"Apakah Anda mengalami {deskripsi.lower()}?" for kode, deskripsi in GEJALA.items()}


# ============================================================
# INFERENCE ENGINE
# ============================================================
def diagnosa(gejala_positif):
    """
    Forward chaining: cocokkan gejala positif dengan basis pengetahuan.
    Kembalikan daftar penyakit dengan skor kecocokan >= 40%.
    """
    hasil = []
    for nama, daftar_gejala in PENYAKIT.items():
        cocok = set(daftar_gejala) & set(gejala_positif)
        if len(cocok) == 0:
            continue
        persen = round(len(cocok) / len(daftar_gejala) * 100)
        if persen >= 40:   # ambang batas minimal 40%
            hasil.append({
                "nama": nama,
                "skor": persen,
                "deskripsi": DESKRIPSI_PENYAKIT.get(nama, "-"),
                "solusi": SARAN_PENYAKIT.get(nama, "-"),
            })
    hasil.sort(key=lambda x: x["skor"], reverse=True)
    return hasil


# ============================================================
# GUI
# ============================================================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.gejala_list = list(PERTANYAAN.keys())
        self.gejala_pos = []
        self.gejala_neg = []
        self.index = 0

        self._build_ui()
        self._set_state_awal()

    def _build_ui(self):
        pad = {"padx": 12, "pady": 6}

        # Judul
        tk.Label(
            self.root,
            text="🩺  Aplikasi Diagnosa Penyakit Telinga Hidung Tenggorokan",
            font=("Segoe UI", 13, "bold"),
            bg="#f0f0f0",
            fg="#1565C0",
        ).grid(row=0, column=0, columnspan=3, padx=16, pady=(14, 4), sticky="w")

        tk.Label(
            self.root,
            text="Jawab pertanyaan berikut sesuai kondisi Anda:",
            bg="#f0f0f0",
            font=("Segoe UI", 9),
            fg="#333",
        ).grid(row=1, column=0, columnspan=3, padx=16, sticky="w")

        # Kotak teks untuk pertanyaan
        self.kotak = tk.Text(
            self.root,
            height=4,
            width=60,
            font=("Segoe UI", 10),
            state="disabled",
            relief="solid",
            bd=1,
            wrap="word",
            padx=8,
            pady=8,
            bg="#ffffff",
            fg="#1A237E",
        )
        self.kotak.grid(row=2, column=0, columnspan=3, padx=16, pady=8)

        # Label progress
        self.progress_label = tk.Label(
            self.root, text="", bg="#f0f0f0", font=("Segoe UI", 8), fg="#666"
        )
        self.progress_label.grid(row=3, column=0, padx=16, sticky="w")

        # Tombol Tidak
        self.btn_tidak = ttk.Button(
            self.root, text="❌  Tidak", width=14,
            command=lambda: self._jawab(False)
        )
        self.btn_tidak.grid(row=3, column=1, **pad, sticky="e")

        # Tombol Ya
        self.btn_ya = ttk.Button(
            self.root, text="✅  Ya", width=14,
            command=lambda: self._jawab(True)
        )
        self.btn_ya.grid(row=3, column=2, **pad, sticky="w")

        # Tombol Mulai / Ulangi
        self.btn_mulai = ttk.Button(
            self.root, text="🔍  Mulai Diagnosa", width=32,
            command=self._mulai
        )
        self.btn_mulai.grid(row=4, column=0, columnspan=3, padx=16, pady=(8, 16))

    def _set_state_awal(self):
        self._tampilkan_teks("Tekan tombol 'Mulai Diagnosa' untuk memulai.")
        self.btn_tidak.configure(state="disabled")
        self.btn_ya.configure(state="disabled")
        self.btn_mulai.configure(state="normal")
        self.progress_label.configure(text="")

    def _mulai(self):
        self.gejala_pos.clear()
        self.gejala_neg.clear()
        self.index = 0
        self.btn_mulai.configure(state="disabled")
        self.btn_tidak.configure(state="normal")
        self.btn_ya.configure(state="normal")
        self._tanya_berikutnya()

    def _tanya_berikutnya(self):
        if self.index >= len(self.gejala_list):
            self._selesai()
            return
        kode_gejala = self.gejala_list[self.index]
        self._tampilkan_teks(PERTANYAAN[kode_gejala])
        self.progress_label.configure(
            text=f"Pertanyaan {self.index + 1} / {len(self.gejala_list)}"
        )

    def _jawab(self, jawaban):
        kode_gejala = self.gejala_list[self.index]
        if jawaban:
            self.gejala_pos.append(kode_gejala)
        else:
            self.gejala_neg.append(kode_gejala)
        self.index += 1
        self._tanya_berikutnya()

    def _selesai(self):
        hasil = diagnosa(self.gejala_pos)
        self._tampilkan_teks("Diagnosa selesai. Hasil akan ditampilkan.")
        self.btn_tidak.configure(state="disabled")
        self.btn_ya.configure(state="disabled")
        self.progress_label.configure(text="")

        # Susun pesan hasil
        if not hasil:
            messagebox.showinfo(
                "Hasil Diagnosa",
                "Berdasarkan gejala yang Anda alami, tidak ditemukan kecocokan yang cukup kuat dengan penyakit yang ada dalam basis pengetahuan.\n\n"
                "Tetap waspada dan konsultasikan ke dokter THT jika keluhan berlanjut.",
            )
        else:
            pesan = ""
            for i, item in enumerate(hasil, 1):
                pesan += (
                    f"{'═'*50}\n"
                    f"[{i}] {item['nama']}\n"
                    f"    Tingkat Kecocokan : {item['skor']}%\n\n"
                    f"    📌 Deskripsi:\n"
                    f"    {item['deskripsi']}\n\n"
                    f"    💊 Saran Penanganan:\n"
                    f"    {item['solusi']}\n\n"
                )
            pesan += (
                f"{'═'*50}\n"
                "⚠️  DISCLAIMER:\n"
                "Hasil diagnosa ini BUKAN pengganti konsultasi dokter.\n"
                "Segera periksakan diri ke tenaga medis profesional."
            )
            messagebox.showinfo("Hasil Diagnosa", pesan)

        self.btn_mulai.configure(state="normal")
        self.btn_mulai.configure(text="🔄  Ulangi Diagnosa")
        # Kembalikan teks tombol jika diulang
        self.btn_mulai.configure(command=self._reset_ulang)

    def _reset_ulang(self):
        """Reset tampilan untuk diagnosa ulang."""
        self.btn_mulai.configure(text="🔍  Mulai Diagnosa", command=self._mulai)
        self._set_state_awal()

    def _tampilkan_teks(self, teks):
        self.kotak.configure(state="normal")
        self.kotak.delete("1.0", "end")
        self.kotak.insert("end", teks)
        self.kotak.configure(state="disabled")


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()