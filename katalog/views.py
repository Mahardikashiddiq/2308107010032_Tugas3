from django.shortcuts import render

# Data produk hardcoded
PRODUK_LIST = [
	{'id': 1, 'nama': 'One Piece Vol. 1', 'deskripsi': 'Petualangan Luffy mencari harta karun legendaris One Piece.', 'harga': 'Rp 35.000'},
	{'id': 2, 'nama': 'Naruto Vol. 1', 'deskripsi': 'Awal kisah ninja Uzumaki Naruto di desa Konoha.', 'harga': 'Rp 32.000'},
	{'id': 3, 'nama': 'Attack on Titan Vol. 1', 'deskripsi': 'Manusia bertahan hidup dari serangan para Titan.', 'harga': 'Rp 38.000'},
	{'id': 4, 'nama': 'Demon Slayer Vol. 1', 'deskripsi': 'Tanjiro berjuang melawan iblis demi keluarganya.', 'harga': 'Rp 36.000'},
	{'id': 5, 'nama': 'My Hero Academia Vol. 1', 'deskripsi': 'Dunia di mana semua orang punya kekuatan super, Izuku ingin jadi pahlawan.', 'harga': 'Rp 34.000'},
	{'id': 6, 'nama': 'Jujutsu Kaisen Vol. 1', 'deskripsi': 'Yuji Itadori bertarung melawan kutukan demi menyelamatkan teman-temannya.', 'harga': 'Rp 37.000'},
	{'id': 7, 'nama': 'Dragon Ball Vol. 1', 'deskripsi': 'Awal petualangan Son Goku mencari bola naga.', 'harga': 'Rp 33.000'},
	{'id': 8, 'nama': 'Detective Conan Vol. 1', 'deskripsi': 'Kasus misteri pertama Shinichi Kudo yang berubah jadi anak kecil.', 'harga': 'Rp 35.000'},
	{'id': 9, 'nama': 'Haikyuu!! Vol. 1', 'deskripsi': 'Hinata Shoyo mengejar impian menjadi pemain voli terbaik.', 'harga': 'Rp 36.000'},
	{'id': 10, 'nama': 'Tokyo Revengers Vol. 1', 'deskripsi': 'Takemichi kembali ke masa lalu untuk menyelamatkan teman-temannya.', 'harga': 'Rp 39.000'},
]

def homepage(request):
	return render(request, 'homepage.html')

def daftar_produk(request):
	return render(request, 'daftar_produk.html', {'produk_list': PRODUK_LIST})

def detail_produk(request, id):
	produk = next((p for p in PRODUK_LIST if p['id'] == id), None)
	return render(request, 'detail_produk.html', {'produk': produk})

def kontak(request):
	return render(request, 'kontak.html')
