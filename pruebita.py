package com.autentia.tutoriales.jtapi;

import javax.telephony.*;

public class RealizarLlamadaApp {
	
	/**
	 * @param args Origen y destino de la llamada
	 */
	public static void main(String[] args){
		Provider prov = null;
		
		// Verificamos los argumentos (número de teléfono de origen y destino)
		if ( args.length != 2 ){
			System.out.println("Formato:\"RealizarLlamadaApp <origen> <destino>\"");
			return;
		}
		
		try {
			// Obtenemos una instancia que implemente javax.telephony.JtapiPeer.
			JtapiPeer peer = JtapiPeerFactory.getJtapiPeer(null);
			
			// Obtenemos un proveedor que de el servicio
			prov = peer.getProvider(null);
			
			//	Instanciamos y configuramos los objetos necesarios para la llamada
			Terminal term = prov.getTerminal(args[0]);
			
			// Creamos un objeto llamada
			Call call = prov.createCall();
			
			// Realizamos una llamada
			call.connect(term, term.getAddresses()[0], args[1]);

		} catch ( Exception e ){
			System.out.println(e.toString());
		} finally {
			try {
				prov.shutdown();	//	Finalizamos el proveedor
			} catch (Exception ex){}
		}
	}
}    