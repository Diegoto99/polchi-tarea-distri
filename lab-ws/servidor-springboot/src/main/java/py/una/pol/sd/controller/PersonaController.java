package py.una.pol.sd.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import py.una.pol.sd.model.Persona;
import py.una.pol.sd.service.PersonaService;

@RestController
@RequestMapping("/personas")
public class PersonaController {

	@Autowired
	PersonaService personaService;

	@GetMapping("/saludo")
	public String index() {
		return "Hola mundo caluroso de Springboot";
	}

    @GetMapping(value = "/listar", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getPersonas() 
	{
		/*List<PersonaDTO> r =  new ArrayList<PersonaDTO>();
		r.add(new PersonaDTO(2000L, "Juan", "Perez"));
		r.add(new PersonaDTO(2001L, "Pedro", "Alonso"));
		r.add(new PersonaDTO(2002L, "Maria", "Lopez"));
		r.add(new PersonaDTO(2003L, "Rosana", "Romero"));
		r.add(new PersonaDTO(2004L, "Liz", "Santos"));
		r.add(new PersonaDTO(2005L, "Luis", "Cabral"));
		*/
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }


	@PostMapping(value = "/crear", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> create(@RequestBody Persona per) {


		if(per != null && per.getCedula() != null) {
			System.out.println("Persona recepcionada "+ per.getNombre());
			
			personaService.crear(per); 

			return new ResponseEntity<>("Se recepcionó correctamente la persona: " + per.toString(), HttpStatus.OK);
		}else{

			System.out.println("Datos mal enviados por el cliente");
			return new ResponseEntity<>("Debe enviar el campo cédula. ", HttpStatus.BAD_REQUEST);
		}


        
    }



}
