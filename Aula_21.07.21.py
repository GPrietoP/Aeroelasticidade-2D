import numpy as np
import matplotlib.pyplot as plt

# Parâmetros analíticos
m = 1 # [kg] - Massa
k = 8 # [N/m] - Rigidez
c = 0 # [N.s/m] -  Amortecimento

delta_t = 10**-2
tempo_inicial = 0.0
tempo_final = 20.0
n_passos = round((tempo_final-tempo_inicial)/delta_t+1)

tempo = np.linspace(tempo_inicial, tempo_final,n_passos)

# Passo simples
acel = np.zeros(n_passos)
vel = np.zeros(n_passos)
pos = np.zeros(n_passos)
pos[0] = 1 # posição inicial
vel[0] = 0 # velocidade inicial
acel[0] = -k/m*pos[0] - c/m*vel[0]
for cont in range(n_passos-1):    
    vel[cont+1] = vel[cont]+acel[cont]*delta_t
    pos[cont+1] = pos[cont]+vel[cont]*delta_t
    acel[cont+1] = -k/m*pos[cont+1] - c/m*vel[cont+1]


# Método dos trapézios
acel_t = np.zeros(n_passos)
vel_t = np.zeros(n_passos)
pos_t = np.zeros(n_passos)
pos_t[0] = 1 # posição inicial
vel_t[0] = 0 # velocidade inicial
acel_t[0] = -k/m*pos_t[0] - c/m*vel_t[0]
for cont in range(n_passos-1):    
    vel_t[cont+1] = vel_t[cont]+acel_t[cont]*delta_t
    pos_t[cont+1] = pos_t[cont]+0.5*(vel_t[cont+1]+vel_t[cont])*delta_t
    acel_t[cont+1] = -k/m*pos_t[cont+1] - c/m*vel_t[cont+1]

# Previsor/Corretor
acel_pc = np.zeros(n_passos)
vel_pc = np.zeros(n_passos)
pos_pc = np.zeros(n_passos)
pos_pc[0] = 1 # posição inicial
vel_pc[0] = 0 # velocidade inicial
acel_pc[0] = -k/m*pos_pc[0] - c/m*vel_pc[0]
for cont in range(n_passos-1):    
    vel_pc[cont+1] = vel_pc[cont]+acel_pc[cont]*delta_t
    pos_pc[cont+1] = pos_pc[cont]+0.5*(vel_pc[cont+1]+vel_pc[cont])*delta_t
    acel_pc[cont+1] = -k/m*pos_pc[cont+1] - c/m*vel_pc[cont+1]
    vel_pc[cont+1] = vel_pc[cont]+0.5*(acel_pc[cont+1]+acel_pc[cont])*delta_t
    pos_pc[cont+1] = pos_pc[cont]+0.5*(vel_pc[cont+1]+vel_pc[cont])*delta_t
    acel_pc[cont+1] = -k/m*pos_pc[cont+1] - c/m*vel_pc[cont+1]

# Resultados analíticos
omega_n = np.sqrt(k/m) # [rad/s]
freq_n = omega_n/(2*np.pi)
zeta = c/(2*np.sqrt(k*m))
omega_a = omega_n*np.sqrt(1-zeta**2)
pos_analitica = pos[0]*np.exp(-zeta*omega_n*tempo)*np.cos(omega_a*tempo)


plt.figure()
plt.plot(tempo, pos, "b", label='Passo simples')
plt.plot(tempo, pos_t, "r", label='Mét. Trapézio')
plt.plot(tempo, pos_pc, "g", label='Preditor/Corretor')
plt.plot(tempo, pos_analitica, "k--", label='Solução Analítica')
plt.title("Comparando métodos de integração no tempo com resultado analítico")
plt.legend()
plt.grid()
plt.show()
