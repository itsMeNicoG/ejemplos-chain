/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package chainOfResponsability;

import java.util.Scanner;
/**
 *
 * @author chamo
 */
public class EjemploChainOfResponsability{

    public static void main(String[] args) {
        EjemploChainOfResponsability ejemplo = new EjemploChainOfResponsability();
        ejemplo.operacion();
    }
    public void operacion() {
        Scanner sc = new Scanner(System.in);
        int opt = 0;
        
        Handler manejadores[] = new Handler[3];
        manejadores[2] = new HandlerOptionDefault();
        manejadores[1] = new HandlerOptionTwo();
        manejadores[0] = new HandlerOptionOne();
        
        for(int i=0; i<manejadores.length - 1;i++){
            manejadores[i].setSuccessor(manejadores[i+1]);
        }
        System.out.println("1) Profesor de catedra");
        System.out.println("2) Profesor de planta");
        System.out.println("ingrese una opcion: ");
        opt =  sc.nextInt();
        
        manejadores[0].handlerRequest(opt);
    }
}
