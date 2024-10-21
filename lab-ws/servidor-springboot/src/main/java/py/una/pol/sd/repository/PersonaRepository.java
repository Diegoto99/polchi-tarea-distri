package py.una.pol.sd.repository;

import java.util.List;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import py.una.pol.sd.model.Persona;

@Repository
public interface PersonaRepository extends CrudRepository<Persona, Integer> {

    List<Persona> findAll();

    List<Persona> findByNombre(String nombre);

    List<Persona> findByApellido(String apellido);

    Persona findByCedula(long id);
}
