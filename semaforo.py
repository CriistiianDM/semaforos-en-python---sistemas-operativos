# definicion de librerias para manejo de hilos y semaforos
import threading , time

# funcion semaforo sem_init
# inicializacion de semaforo
def sem_init(sem, val):
    sem.value = val


# funcion semaforo sem_wait
# decremento de semaforo
def sem_wait(sem):
    sem.acquire()

# funcion semaforo sem_post
# incremento de semaforo
def sem_post(sem):
    sem.release()


#cuerpo del hilo padre
def padre_cuerpo():
    i = 0
    #bucle infinito
    while True:
        print("Hola, soy el padre",i)
        if i == 2500:
            #depierta el hijo
            hilo_hijo.start()
            #espera a que termine el hilo hijo
            sem_wait(sem)
          
        if i == 5000:
            #mensaje de terminacion
            print("ejecusion del padre termino",i)
            #terminar el hilo padre
            break
        i += 1
    print('sali')
   

  
# cuerpo del hilo hijo
def hijo_cuerpo():
    i = 0
    #bucle infinito
    while True:
        print("Hola, soy el hijo",i)
        if i == 2500:
            #poner a dormir el hilo
            time.sleep(10)
            #mensaje de terminacion
            print("ejecusion del hijo termino",i)
            #despertar al padre
            sem_post(sem)
            #terminar el hilo hijo
            break
        i += 1

  
#creacion del semaforo
sem = threading.Semaphore(0)

#ejecucion de un hilo padre con su cuerpo
hilo_padre = threading.Thread(target=padre_cuerpo)
hilo_hijo = threading.Thread(target=hijo_cuerpo)
hilo_padre.start()
hilo_padre.join()