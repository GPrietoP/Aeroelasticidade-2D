import numpy as np
import matplotlib.pyplot as plt

# Parâmetros analíticos
m = 1 # [kg] - Massa
k = 4 # [N/m] - Rigidez
c = 0.8 # [N.s/m] -  Amortecimento

# Resultados analíticos
omega_n = np.sqrt(k/m) # [rad/s]
freq_n = omega_n/(2*np.pi)
zeta = c/(2*np.sqrt(k*m))

print("omega_n = ", round(omega_n,2), "rad/s   freq_n = ", round(freq_n, 2), "Hz   zeta = ", round(zeta,2))

# Resolução no tempo
n_iteracoes = 1000
tempo = np.linspace(0, 50, n_iteracoes)
delta_t = tempo[1]-tempo[0]
acel = np.zeros(n_iteracoes)
vel = np.zeros(n_iteracoes)
pos = np.zeros(n_iteracoes)
# Condições iniciais
pos[0] = 2 # [m]
vel[0] = 0 # [m/s]

for cont, _t in enumerate(tempo):
     acel[cont] = (-k*pos[cont]-c*vel[cont])/m
     if cont<n_iteracoes-1:
         vel[cont+1] = vel[cont]+acel[cont]*delta_t
         pos[cont+1] = pos[cont]+vel[cont]*delta_t

# plt.figure()
# plt.plot(tempo, pos, 'b')
# plt.show()

intensidade_ruido = 0.08*max(pos)
pos_ruido = pos+intensidade_ruido*(np.random.random(len(pos))-0.5)

# plt.figure()
# plt.plot(tempo, pos, 'b')
# plt.plot(tempo, pos_ruido, 'r')
# plt.show()

pos_analitica = pos[0]*np.exp(-zeta*omega_n*tempo)*np.cos(omega_n*tempo)

plt.figure()
plt.plot(tempo, pos, 'b')
plt.plot(tempo, pos_analitica, 'g')
plt.plot(tempo, pos_ruido, 'r')
plt.show()

###
#### Encontra Maximos
#### Recorte
###


