def perkeni(berat_badan, tinggi_badan, umur, gender, faktor_aktivitas):
    # Kategori faktor usia
    if umur >= 0 and umur < 41:
        faktor_usia = 0
    elif umur > 39 and umur < 60:
        faktor_usia = 5
    elif umur > 59 and umur < 70:
        faktor_usia = 10
    elif umur > 69:
        faktor_usia = 15

    # Konversi faktor usia ke persentase
    persen_faktor_usia = faktor_usia / 100

    # Kategori faktor aktivitas
    if faktor_aktivitas == 'bedrest':
        aktivitas = 10
    elif faktor_aktivitas == 'ringan':
        aktivitas = 20
    elif faktor_aktivitas == 'sedang':
        aktivitas = 30
    elif faktor_aktivitas == 'berat':
        aktivitas = 40
    elif faktor_aktivitas == 'sangat berat':
        aktivitas = 50

    # Konversi aktivitas ke persentase
    persen_aktivitas = aktivitas / 100

    # Perhitungan berat badan ideal
    if gender == 'pria':
        bbi = (tinggi_badan - 100) - ((tinggi_badan - 100) * 10 / 100)
    else:
        bbi = (tinggi_badan - 100) + ((tinggi_badan - 100) * 15 / 100)

    # Perhitungan BMR (Basal Metabolic Rate)
    if gender == 'pria':
        bmr = 30 * bbi
    else:
        bmr = 25 * bbi



    bmr = bmr
    bbi = bbi
    imt = berat_badan/(tinggi_badan/100)**2
    # Perhitungan energi
    energi = (bmr + ((persen_aktivitas) * bmr)) - (persen_faktor_usia * bmr)
    protein = 0.15 * energi / 4
    lemak = 0.25 * energi / 9
    karbo = 0.65 * energi / 4
    gula = 0.05*energi/4
    gula_sendok = karbo/gula

    # perhitungan sekali makan
    energi_pagi = 0.35 * energi
    protein_pagi = 0.35 * protein
    lemak_pagi = 0.35 * lemak
    karbo_pagi = 0.35 * karbo

    energi_malam = 0.30 * energi
    protein_malam = 0.30 * protein
    lemak_malam = 0.30 * lemak
    karbo_malam = 0.30 * karbo

    return {'energi':energi, 'protein':protein, 'lemak':lemak, 'karbo':karbo,
            'energi_pagi':energi_pagi, 'protein_pagi':protein_pagi, 'lemak_pagi':lemak_pagi, 'karbo_pagi':karbo_pagi,
            'energi_malam':energi_malam, 'protein_malam':protein_malam, 'lemak_malam':lemak_malam, 'karbo_malam':karbo_malam,
            'imt':imt, 'bbi':bbi, 'bmr':bmr, 'gula':gula, 'gula_sendok':gula_sendok
            }

# gula 2 jam 
def gd2pp(nilai):
  if nilai < 110:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Rendah',
        'rujukan' : '110 - 145 mg/dL',
    }
  elif nilai <= 110 and nilai <=145:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Normal',
        'rujukan' : '110 - 145 mg/dL',
    }
  elif nilai > 145:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Tinggi',
        'rujukan' : '110 - 145 mg/dL',
    }

# gula darah puasa
def gdp(nilai):
  if nilai < 80:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Rendah',
        'rujukan' : '80 - 110 mg/dL',
    }
  elif nilai <= 80 and nilai <=110:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Normal',
        'rujukan' : '80 - 110 mg/dL',
    }
  elif nilai > 110:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Tinggi',
        'rujukan' : '80 - 110 mg/dL',
    }

# gula darah Sewaktu
def gds(nilai):
  if nilai < 70:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Rendah',
        'rujukan' : '70-200 mg/dl',
    }
  elif nilai <= 70 and nilai <=200:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Normal',
        'rujukan' : '70-200 mg/dl',
    }
  elif nilai > 200:
    hasil={
        'value' : f"{nilai} mg/dL",
        'hasil' : 'Tinggi',
        'rujukan' : '70-200 mg/dl',
    }
