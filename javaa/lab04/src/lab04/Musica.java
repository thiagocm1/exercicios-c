package lab04;

public class Musica {
	private String titulo;
	    private int duracao;
	    private String tipo;
	   
	    public Musica(String titulo, int duracao, String tipo) throws Exception{
	        if(titulo == null || titulo.trim().isEmpty()){
	            throw new Exception("Não é permitido o titulo ser nulo ou vazio.");
	        }
	        if(duracao <= 0){
	            throw new Exception("Não é permitido a duração da música ser menor que 0.");
	        }
	        if(tipo == null || tipo.trim().isEmpty()){
	            throw new Exception("Não é permitido o titulo ser nulo ou vazio");
	        }
	        this.titulo = titulo;
	        this.duracao = duracao;
	        this.tipo = tipo;
	    }
	   
	    public String getTitulo() {
	        return titulo;
	    }

	    public void setTitulo(String titulo) {
	        this.titulo = titulo;
	    }

	    public int getDuracao() {
	        return duracao;
	    }

	    public void setDuracao(int duracao) {
	        this.duracao = duracao;
	    }

	    public String getTipo() {
	        return tipo;
	    }

	    public void setTipo(String tipo) {
	        this.tipo = tipo;
	    }
		@Override
		public boolean equals(Object outraMusica){
			if(outraMusica instanceof Musica){
				Musica musica = (Musica) outraMusica;
				return (this.titulo.equalsIgnoreCase(musica.getTitulo()) && this.duracao == musica.getDuracao());
			}return false;
		}
}
