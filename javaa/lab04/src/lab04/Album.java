package lab04;

import java.util.ArrayList;
import java.util.List;

public class Album {
	Musica novaMusica;
	private String artista;
	private String tituloAlbum;
	private final int ANO_LANCAMENTO = 1900;
	private List<Musica> musicas;
	private int anoLancamento;
	private int duracaoAlbum = 0;

	public Album(String artista, String tituloAlbum, int anoLancamento) throws Exception {
		if (artista == null || artista.trim().isEmpty()) {
			throw new Exception("Artista do album nao pode ser nulo ou vazio.");
		}
		if (anoLancamento <= ANO_LANCAMENTO) {
			throw new Exception("Ano de lancamento do album nao pode ser inferior a 1900.");
		}
		
		if (tituloAlbum == null || tituloAlbum.trim().isEmpty()) {
			throw new Exception("Titulo do album nao pode ser nulo ou vazio.");
		}

		this.artista = artista;
		this.tituloAlbum = tituloAlbum;
		this.anoLancamento = anoLancamento;
		musicas = new ArrayList<Musica>();
	}

	public boolean adicionaMusica(Musica novaMusica) throws Exception{
	if(novaMusica != null){
		this.musicas.add(novaMusica);
		return true;
		} return false;
	}
		


	public boolean removeMusica(int faixa){
		for(int i = 0; i < musicas.size(); i++){
			musicas.remove(faixa-1);
			return true;
		}return false;
	}

	public boolean contemMusica(String titulo){
		for (Musica musica : musicas) {
			if(musica.getTitulo().equals(titulo)){
				return true;
			}
		}return false;
	}
	public int getDuracaoTotal() {
		for (int i = 0; i < musicas.size(); i++) {
			duracaoAlbum += musicas.get(i).getDuracao();
		}
		return duracaoAlbum;
	}
	
	public Musica getMusica(int faixa){
		return musicas.get(faixa - 1);
	}
	public Musica getMusica(String titulo){
		for (Musica musica : musicas) {
			if(musica.getTitulo().equalsIgnoreCase(titulo)){
				return musica;
			}
		}return null;
	}
	@Override
	public boolean equals(Object outroAlbum){
		if(outroAlbum instanceof Album){
			Album novoAlbum = (Album) outroAlbum;
			return this.getTituloAlbum().equals(((Album) outroAlbum).getTituloAlbum()) && this.getArtista().equals(((Album) outroAlbum).getArtista());
		}return false;
	}

	public int quantidadeFaixas(){
		return musicas.size();
	}

	public Musica getNovaMusica() {
		return novaMusica;
	}

	public void setNovaMusica(Musica novaMusica) {
		this.novaMusica = novaMusica;
	}

	public String getArtista() {
		return artista;
	}

	public void setArtista(String artista) {
		this.artista = artista;
	}

	public String getTituloAlbum() {
		return tituloAlbum;
	}

	public void setTituloAlbum(String tituloAlbum) {
		this.tituloAlbum = tituloAlbum;
	}

	public List<Musica> getMusicas() {
		return musicas;
	}

	public void setMusicas(List<Musica> musicas) {
		this.musicas = musicas;
	}

	public int getAnoLancamento() {
		return anoLancamento;
	}

	public void setAnoLancamento(int anoLancamento) {
		this.anoLancamento = anoLancamento;
	}

	public int getDuracaoAlbum() {
		return duracaoAlbum;
	}

	public void setDuracaoAlbum(int duracaoAlbum) {
		this.duracaoAlbum = duracaoAlbum;
	}
}

