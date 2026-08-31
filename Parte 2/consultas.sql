-- Listar todos los productos disponibles con stock menor a 10 unidades.
SELECT Nombre, Precio, Stock
FROM Producto
WHERE Stock < 10;

-- Calcular el promedio de precios de productos por cada categoría existente.
SELECT C.Nombre AS Categoria, AVG(P.Precio) AS PromedioPrecio
FROM Producto P
JOIN Categoria C ON P.IdCategoria = C.IdCategoria
GROUP BY C.Nombre;