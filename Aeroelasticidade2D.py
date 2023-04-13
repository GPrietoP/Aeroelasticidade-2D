import numpy as np

## ANALISANDO A DIVERGÊNCIA 2D

# Características do perfil
perfil = "Naca0012"
## Estes parâmetros podem ser determinados por método dos paineis, VLM, Literatura
a0 = 0
a1 = 2*np.pi # resultado potencial para placa plana
b0 = 0 # coeficiente de momento de arfagem
corda = 1 # Metro

centro_aerodinamico = 0.25
centro_elastico = 0.3 # posição percentural ao longo da corda, partindo do bordo de ataque
e = centro_elastico - centro_aerodinamico

## ANALISE RIGIDA
angulo_de_ataque_original = 2*(np.pi/180) # Rad
coef_sustentacao = a0 + a1*angulo_de_ataque_original

rho = 1.224 # Kg/m**3 densidade do ar ao nível do solo
vel_voo = 14 # m/s
q = 0.5*rho*(vel_voo**2) # pressão dinâmica Pa
sustentacao_rigida = q*coef_sustentacao*corda # N/m

coef_momento_arfagem = b0 # b1 será zero
momento_arfagem = q*coef_momento_arfagem*corda**2 # N.m/m
momento_total = momento_arfagem + sustentacao_rigida * (e*corda)

## ANÁLISE FLEXÍVEL
rigidez_torcional = 50 # (Nm/m)/rad
torcao = momento_total/rigidez_torcional # em modelos mais completos - FEM
angulo_de_ataque = angulo_de_ataque_original + torcao
print("_"*80) 
print(" ")
print(f"L = {round(sustentacao_rigida,2)} N/m   Mtotal = {round(momento_total, 2)} N/m   Torção = {round(torcao*180/np.pi,3)} graus"
        f"   Ângulo de Ataque = {round(angulo_de_ataque*180/np.pi, 3)} graus")

coef_sustentacao=a0+a1*angulo_de_ataque
sustentacao = q*coef_sustentacao*corda
momento_total = momento_arfagem+sustentacao* (e*corda)
torcao = momento_total/rigidez_torcional
angulo_de_ataque = angulo_de_ataque_original + torcao
print(f"L = {round(sustentacao,2)} N/m   Mtotal = {round(momento_total, 2)} N/m   Torção = {round(torcao*180/np.pi,3)} graus"
        f"   Ângulo de Ataque = {round(angulo_de_ataque*180/np.pi, 3)} graus")


n_iteracoes = 30
angulo_de_ataque = angulo_de_ataque_original

for iteração in range(n_iteracoes):
    coef_sustentacao=a0+a1*angulo_de_ataque
    sustentacao = q*coef_sustentacao*corda    
    momento_total = momento_arfagem+sustentacao* (e*corda)
    torcao = momento_total/rigidez_torcional
    angulo_de_ataque = angulo_de_ataque_original + torcao    
    print(f"L = {round(sustentacao,2)} N/m   Mtotal = {round(momento_total, 2)} N/m   Torção = {round(torcao*180/np.pi,3)} graus"
        f"   Ângulo de Ataque = {round(angulo_de_ataque*180/np.pi, 3)} graus")

print("_"*80) 
print(" ")
# Valores final calculados pela formúla analítica com simplificações
R = ((corda**2)*a1*e)/rigidez_torcional
q_divergencia = 1/R
vel_divergencia = np.sqrt(2*q_divergencia/rho)
torcao_final = angulo_de_ataque_original*q*R/(1-q*R)
angulo_de_ataque_final = angulo_de_ataque_original+torcao_final
print(f"Velocidade de Voo = {round(vel_voo,3)} m/s")
print("Velocidade de divergência = ", round(vel_divergencia,2), "m/s")
print(f"Ângulo de Ataque final = {round(angulo_de_ataque_final*180/np.pi,4)} graus")
print(f"Torção final = {round(torcao_final*180/np.pi,4)} graus")
#print(f"Ângulo de Ataque Teórico = {round()}")