package main

import (
    "fmt"
    "strings"
)

// Función que saluda al usuario según su nombre
func saludar(nombre string) string {
    return "¡Hola, " + strings.Title(nombre) + "! Bienvenido."
}

// Función que evalúa si un número es par o impar
func esPar(n int) bool {
    return n%2 == 0
}

func main() {
    // 🔹 Declaración de variables simples
    var nombre string
    var edad int
    var cursoActivo bool = false

    // 🔹 Entrada básica
    fmt.Print("- Ingresa tu nombre: ")
    fmt.Scanln(&nombre)

    fmt.Print("- Ingresa tu edad: ")
    fmt.Scanln(&edad)

    // 🔹 Salida básica
    fmt.Println(saludar(nombre))

    // 🔹 Estructura condicional: if
    if edad >= 18 {
        fmt.Println("  Eres mayor de edad.")
        cursoActivo = true
    } else {
        fmt.Println("  Aún no eres mayor de edad.")
    }

    // 🔹 Estructura iterativa: for
    fmt.Println("  Mostrando los números pares hasta tu edad:")
    for i := 1; i <= edad; i++ {
        if esPar(i) {
            fmt.Print("  ", i)
        }
    }
    fmt.Println()

    // 🔹 Estructura de control: switch
    switch cursoActivo {
    case true:
        fmt.Println("  El curso está activo. ¡A estudiar!")
    case false:
        fmt.Println("  El curso no está activo por ahora.")
    }

    // 🔹 Fin del programa
    fmt.Println("Programa finalizado.")
}
