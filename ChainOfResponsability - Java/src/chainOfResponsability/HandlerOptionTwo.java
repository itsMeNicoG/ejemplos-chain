package chainOfResponsability;
public class HandlerOptionTwo extends Handler{

    @Override
    public void handlerRequest(int opt) {
        if(opt == 2){
            System.out.println("Calculando la nomina de un profesor de planta");
        }else{
            successor.handlerRequest(opt);
        }
    }
    
}
