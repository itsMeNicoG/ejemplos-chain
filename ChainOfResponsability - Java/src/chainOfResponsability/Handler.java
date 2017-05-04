package chainOfResponsability;
public abstract class Handler {
    Handler successor;
    
    public abstract void handlerRequest(int opt);

    public Handler getSuccessor() {
        return successor;
    }

    public void setSuccessor(Handler successor) {
        this.successor = successor;
    }
        
    
    
}
