CREATE TABLE Categoria (
    IdCategoria INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Producto (
    IdProducto INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL,
    Tipo VARCHAR(20) NOT NULL, 
    IdCategoria INT,
    FOREIGN KEY (IdCategoria) REFERENCES Categoria(IdCategoria)
);