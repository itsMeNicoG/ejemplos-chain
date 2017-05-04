package chainOfResponsability;
public class HandlerOptionOne extends Handler{

    @Override
    public void handlerRequest(int opt) {
        if(opt == 1){
            System.out.println("Calculando la nomina de un profesor de catedra");
        }else{
            successor.handlerRequest(opt);
        }
    }
    
}
