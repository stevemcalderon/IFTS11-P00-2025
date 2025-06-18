class GestorAdopciones:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def eliminar_perro_por_nombre(self, nombre):
        for perro in self.perros:
            if perro.nombre == nombre:
                self.perros.remove(perro)
                print(f"Perro '{nombre}' eliminado del sistema.")
                break
        else:
            print("No se encontró ningún perro con ese nombre.")
        print("Lista actualizada de perros:", self.perros)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def reservar_perro(self, perro_id):
        for perro in self.perros:
            if perro.id == perro_id:
                if perro.estado == "disponible":
                    perro.cambiar_estado("reservado")
                    print(f"Perro {perro_id} fue reservado exitosamente.")
                    return perro
                else:
                    print(f"El perro con ID {perro_id} ya está reservado.")
                    return None
        print(f"No existe un perro con ID {perro_id}.")
        return None

    def confirmar_adopcion(self, perro_id, usuario_dni):
        perro_encontrado = next((p for p in self.perros if p.id == perro_id and p.estado == "reservado"), None)
        if not perro_encontrado:
            raise ValueError(f"No se encontró un perro reservado con ID {perro_id}.")

        usuario_encontrado = next((u for u in self.usuarios if u.dni == usuario_dni), None)
        if not usuario_encontrado:
            raise ValueError(f"No se encontró un usuario con DNI {usuario_dni}.")

        perro_encontrado.cambiar_estado("adoptado")
        usuario_encontrado.historial_adopciones.append(perro_encontrado)
        print(f"¡Adopción confirmada! {perro_encontrado.nombre} ahora es parte de la familia de {usuario_encontrado.nombre}.")

    def sugerir_perro_por_preferencia(self, dni_usuario):
        usuario = next((u for u in self.usuarios if u.dni == dni_usuario), None)
        if not usuario:
            print("Usuario no encontrado.")
            return

        preferencias = usuario.preferencias
        sugerencias = [p for p in self.perros if p.estado == "disponible" and p.raza == preferencias]

        for sugerencia in sugerencias:
            print(f"Recomendación: {sugerencia.nombre}")
