package py.una.pol.sd.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import py.una.pol.sd.model.Persona;
import py.una.pol.sd.repository.PersonaRepository;

@Service
public class PersonaService {


    @Autowired
    PersonaRepository repository;
  
    public List<Persona> getPersonas(){

        return repository.findAll();
    }
    
    public Persona crear(Persona p){

        return repository.save(p);
    }


    public Persona buscarPorCedula(Integer cedula) {
        return repository.findById(cedula).orElse(null);
    }
    
    public Persona actualizar(Persona p) {
        return repository.save(p);
    }
    
    public void borrar(Integer cedula) {
        repository.deleteById(cedula);
    }
    
}
