const CACHE_NAME = 'tienda-geek-v1';
const RECURSOS_A_GUARDAR = [
    './',
    './index.html',
    './manifest.json'
];

// FASE 1: INSTALACIÓN (Guardar la interfaz en caché)
self.addEventListener('install', evento => {
    evento.waitUntil(
        caches.open(CACHE_NAME)
        .then(cache => {
            console.log("Archivos cacheados exitosamente");
            return cache.addAll(RECURSOS_A_GUARDAR);
        })
    );
});

// FASE 2: INTERCEPTAR RED (Estrategia "Cache First")
self.addEventListener('fetch', evento => {
    evento.respondWith(
        caches.match(evento.request)
        .then(respuestaCache => {
            // Si el archivo está en el caché, devuélvelo (Offline)
            if (respuestaCache) {
                return respuestaCache;
            }
            // Si no está en el caché, ve a buscarlo a internet (Online)
            return fetch(evento.request);
        })
    );
});