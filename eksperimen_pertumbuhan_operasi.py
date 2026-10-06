"""Eksperimen pertumbuhan jumlah operasi: O(n) dan O(n^2)."""

from pathlib import Path

import matplotlib.pyplot as plt


NILAI_N = [1, 2, 3, 4, 5, 10, 20]
OUTPUT_DIR = Path(__file__).resolve().parent / "hasil"


def hitung_linear(n: int) -> int:
    """Menghitung operasi pada satu perulangan sebanyak n kali."""
    operasi = 0
    for _ in range(n):
        operasi += 1
    return operasi


def hitung_grid(n: int) -> int:
    """Menghitung operasi pada dua perulangan bersarang n x n."""
    operasi = 0
    for _ in range(n):
        for _ in range(n):
            operasi += 1
    return operasi


def buat_grafik() -> None:
    """Menyimpan grafik kuadrat dan grafik perbandingan."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    linear = [hitung_linear(n) for n in NILAI_N]
    kuadrat = [hitung_grid(n) for n in NILAI_N]

    plt.figure(figsize=(8, 5))
    plt.plot(NILAI_N, kuadrat, marker="o", color="#d97706", linewidth=2)
    plt.xlabel("Jumlah Data (n)")
    plt.ylabel("Jumlah Operasi")
    plt.title("Pertumbuhan Jumlah Operasi")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "grafik_pertumbuhan_grid.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.plot(
        NILAI_N,
        linear,
        marker="o",
        label="Satu Perulangan - O(n)",
        linewidth=2,
    )
    plt.plot(
        NILAI_N,
        kuadrat,
        marker="o",
        label="Dua Perulangan - O(n^2)",
        linewidth=2,
    )
    plt.xlabel("Jumlah Data (n)")
    plt.ylabel("Jumlah Operasi")
    plt.title("Perbandingan Pertumbuhan Operasi")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "grafik_perbandingan.png", dpi=180)
    plt.close()


def tampilkan_hasil() -> None:
    """Menampilkan hasil eksperimen dalam bentuk tabel di terminal."""
    print("EKSPERIMEN 1 - SATU PERULANGAN")
    print("n  | jumlah operasi")
    for n in [5, 10, 20]:
        print(f"{n:<2} | {hitung_linear(n)}")

    print("\nEKSPERIMEN 2 - DUA PERULANGAN")
    print("n  | jumlah operasi")
    for n in [3, 5, 10]:
        print(f"{n:<2} | {hitung_grid(n)}")

    print("\nPERBANDINGAN")
    print("n  | satu perulangan | dua perulangan")
    for n in [5, 10, 20]:
        print(f"{n:<2} | {hitung_linear(n):<15} | {hitung_grid(n)}")


if __name__ == "__main__":
    tampilkan_hasil()
    buat_grafik()
    print(f"\nGrafik tersimpan di: {OUTPUT_DIR}")
