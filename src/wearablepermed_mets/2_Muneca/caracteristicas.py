
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def getFFTpower(FFT, normalize=True):
    n = len(FFT)
    FFTpow = FFT * np.conjugate(FFT)
    FFTpow = FFTpow.real
    if normalize:
        FFTpow = FFTpow / (n * n)
    return FFTpow


def frecuencia_armonico_dominante(v, fm):
    n = len(v)
    vMean = np.mean(v)
    vFFT = v - vMean
    vFFT = vFFT * np.hanning(n)
    
    # Realizar FFT
    vFFT = np.fft.rfft(vFFT)
    vFFTpow = getFFTpower(vFFT)
    
    # Encontrar las frecuencias dominantes
    FFTinterval = fm / (1.0 * n)  # Resolución en Hz
    f1_idx = np.argmax(vFFTpow)   # Índice del máximo de potencia
    p1 = vFFTpow[f1_idx]          # Potencia máxima
    f1 = f1_idx * FFTinterval     # Frecuencia en Hz
    
    # Descartamos el primer pico para encontrar el siguiente
    vFFTpow[f1_idx] = 0  
    f2_idx = np.argmax(vFFTpow)  # Índice del segundo máximo de potencia
    p2 = vFFTpow[f2_idx]         # Potencia del segundo pico
    f2 = f2_idx * FFTinterval    # Frecuencia en Hz
    
    # Cálculo de la entropía espectral
    vFFTpowsum = np.sum(vFFTpow)                                # Suma total de las potencias FFT
    p = vFFTpow / (vFFTpowsum + 1e-8)                           # Probabilidades normalizadas
    spectralEntropy = np.sum(-p * np.log10(p + 1E-8))           # Entropía espectral
    spectralEntropy = spectralEntropy / np.log10(len(vFFTpow))  # Normalizamos la entropía
    
    return f1


def potencia_armonico_dominante(v, fm):
    n = len(v)
    vMean = np.mean(v)
    vFFT = v - vMean
    vFFT = vFFT * np.hanning(n)
    
    # Realizar FFT
    vFFT = np.fft.rfft(vFFT)
    vFFTpow = getFFTpower(vFFT)
    
    # Encontrar las frecuencias dominantes
    FFTinterval = fm / (1.0 * n)  # Resolución en Hz
    f1_idx = np.argmax(vFFTpow)   # Índice del máximo de potencia
    p1 = vFFTpow[f1_idx]          # Potencia máxima
    f1 = f1_idx * FFTinterval     # Frecuencia en Hz
    
    # Descartamos el primer pico para encontrar el siguiente
    vFFTpow[f1_idx] = 0  
    f2_idx = np.argmax(vFFTpow)  # Índice del segundo máximo de potencia
    p2 = vFFTpow[f2_idx]         # Potencia del segundo pico
    f2 = f2_idx * FFTinterval    # Frecuencia en Hz
    
    # Cálculo de la entropía espectral
    vFFTpowsum = np.sum(vFFTpow)                                # Suma total de las potencias FFT
    p = vFFTpow / (vFFTpowsum + 1e-8)                           # Probabilidades normalizadas
    spectralEntropy = np.sum(-p * np.log10(p + 1E-8))           # Entropía espectral
    spectralEntropy = spectralEntropy / np.log10(len(vFFTpow))  # Normalizamos la entropía
    
    return p1



def frecuencia_armonico_2_dominante(v, fm):
    n = len(v)
    vMean = np.mean(v)
    vFFT = v - vMean
    vFFT = vFFT * np.hanning(n)
    
    # Realizar FFT
    vFFT = np.fft.rfft(vFFT)
    vFFTpow = getFFTpower(vFFT)
    
    # Encontrar las frecuencias dominantes
    FFTinterval = fm / (1.0 * n)  # Resolución en Hz
    f1_idx = np.argmax(vFFTpow)   # Índice del máximo de potencia
    p1 = vFFTpow[f1_idx]          # Potencia máxima
    f1 = f1_idx * FFTinterval     # Frecuencia en Hz
    
    # Descartamos el primer pico para encontrar el siguiente
    vFFTpow[f1_idx] = 0  
    f2_idx = np.argmax(vFFTpow)  # Índice del segundo máximo de potencia
    p2 = vFFTpow[f2_idx]         # Potencia del segundo pico
    f2 = f2_idx * FFTinterval    # Frecuencia en Hz
    
    # Cálculo de la entropía espectral
    vFFTpowsum = np.sum(vFFTpow)                                # Suma total de las potencias FFT
    p = vFFTpow / (vFFTpowsum + 1e-8)                           # Probabilidades normalizadas
    spectralEntropy = np.sum(-p * np.log10(p + 1E-8))           # Entropía espectral
    spectralEntropy = spectralEntropy / np.log10(len(vFFTpow))  # Normalizamos la entropía
    
    return f2



def potencia_armonico_2_dominante(v, fm):
    n = len(v)
    vMean = np.mean(v)
    vFFT = v - vMean
    vFFT = vFFT * np.hanning(n)
    
    # Realizar FFT
    vFFT = np.fft.rfft(vFFT)
    vFFTpow = getFFTpower(vFFT)
    
    # Encontrar las frecuencias dominantes
    FFTinterval = fm / (1.0 * n)  # Resolución en Hz
    f1_idx = np.argmax(vFFTpow)   # Índice del máximo de potencia
    p1 = vFFTpow[f1_idx]          # Potencia máxima
    f1 = f1_idx * FFTinterval     # Frecuencia en Hz
    
    # Descartamos el primer pico para encontrar el siguiente
    vFFTpow[f1_idx] = 0  
    f2_idx = np.argmax(vFFTpow)  # Índice del segundo máximo de potencia
    p2 = vFFTpow[f2_idx]         # Potencia del segundo pico
    f2 = f2_idx * FFTinterval    # Frecuencia en Hz
    
    # Cálculo de la entropía espectral
    vFFTpowsum = np.sum(vFFTpow)                                # Suma total de las potencias FFT
    p = vFFTpow / (vFFTpowsum + 1e-8)                           # Probabilidades normalizadas
    spectralEntropy = np.sum(-p * np.log10(p + 1E-8))           # Entropía espectral
    spectralEntropy = spectralEntropy / np.log10(len(vFFTpow))  # Normalizamos la entropía
    
    return p2


def spectral_entropy(v, fm):
    n = len(v)
    vMean = np.mean(v)
    vFFT = v - vMean
    vFFT = vFFT * np.hanning(n)
    
    # Realizar FFT
    vFFT = np.fft.rfft(vFFT)
    vFFTpow = getFFTpower(vFFT)
    
    # Encontrar las frecuencias dominantes
    FFTinterval = fm / (1.0 * n)  # Resolución en Hz
    f1_idx = np.argmax(vFFTpow)   # Índice del máximo de potencia
    p1 = vFFTpow[f1_idx]          # Potencia máxima
    f1 = f1_idx * FFTinterval     # Frecuencia en Hz
    
    # Descartamos el primer pico para encontrar el siguiente
    vFFTpow[f1_idx] = 0  
    f2_idx = np.argmax(vFFTpow)  # Índice del segundo máximo de potencia
    p2 = vFFTpow[f2_idx]         # Potencia del segundo pico
    f2 = f2_idx * FFTinterval    # Frecuencia en Hz
    
    # Cálculo de la entropía espectral
    vFFTpowsum = np.sum(vFFTpow)                                # Suma total de las potencias FFT
    p = vFFTpow / (vFFTpowsum + 1e-8)                           # Probabilidades normalizadas
    spectralEntropy = np.sum(-p * np.log10(p + 1E-8))           # Entropía espectral
    spectralEntropy = spectralEntropy / np.log10(len(vFFTpow))  # Normalizamos la entropía
    
    return spectralEntropy


def numero_picos(group):

    indices_picos, _ = find_peaks(group)
    return len(indices_picos)


def prominencia_media(group):
    
    indices_picos, propiedades_picos = find_peaks(group, prominence=True)
    
    if len(indices_picos) > 0:
        prominencias_picos = propiedades_picos['prominences']
        prominencia_media = np.median(prominencias_picos)
    else:
        prominencia_media = 0
    
    return prominencia_media


def autocorrelacion_desplazada(serie, lag=25):
    serie = serie.values  # asegurar array numpy
    if len(serie) <= lag:
        return np.nan  # No se puede calcular si la serie es muy corta
    serie_desplazada = np.empty_like(serie)
    serie_desplazada[:lag] = 0
    serie_desplazada[lag:] = serie[:-lag]
    return np.corrcoef(serie, serie_desplazada)[0,1]



def calcular_roll_pitch_yaw(acc_x, acc_y, acc_z, gyr_z, dt=1/25):
    yaw_acumulado = 0
    rolls = []
    pitches = []
    yaws = []
    
    for i in range(len(acc_x)):
        roll = np.atan2(acc_y[i], acc_z[i])
        pitch = np.atan2(-acc_x[i], np.sqrt(acc_y[i]**2 + acc_z[i]**2))
        yaw_acumulado += gyr_z[i] * dt
        
        rolls.append(roll)
        pitches.append(pitch)
        yaws.append(yaw_acumulado)
    
    return np.mean(rolls), np.mean(pitches), np.mean(yaws)