tamu = ["Ningguang", "Hutao", "Xiao", "Childe"]

indeks_xiao = tamu.index("Xiao") 
    
tersangka = tamu[indeks_xiao + 1] 
print(f"- {tersangka} adalah tamu terakhir yang masuk setelah Xiao.")
print(f"- Karena kue masih ada saat Xiao masuk, tetapi hilang setelah semua tamu masuk, maka {tersangka} adalah yang paling mungkin mengambil kue.")
    


print(f"\nKesimpulan: Pelaku yang paling mungkin mengambil kue adalah: {tersangka}")