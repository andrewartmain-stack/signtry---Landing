(function () {
    var nav = document.querySelector('nav'), burger = document.getElementById('burger'), dds = document.querySelectorAll('.dd');

    function closeAll(except) {
        dds.forEach(function (d) { if (d !== except) { d.classList.remove('open'); d.querySelector('button').setAttribute('aria-expanded', false) } });
    }

    dds.forEach(function (dd) {
        var btn = dd.querySelector('button');
        btn.onclick = function (e) { e.stopPropagation(); closeAll(dd); var o = dd.classList.toggle('open'); btn.setAttribute('aria-expanded', o) };
    });
    document.addEventListener('click', function (e) { if (!e.target.closest('.dd')) closeAll() });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { closeAll(); nav.classList.remove('open'); burger.setAttribute('aria-expanded', false) }
    });
    burger.onclick = function () { var o = nav.classList.toggle('open'); burger.setAttribute('aria-expanded', o) };
    document.querySelectorAll('#links a').forEach(function (a) {
        a.addEventListener('click', function () { nav.classList.remove('open'); burger.setAttribute('aria-expanded', false) });
    });

    // Play videos only while they are on screen
    var vids = document.querySelectorAll('video');
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (es) {
            es.forEach(function (e) { if (e.isIntersecting) { var p = e.target.play(); if (p) p.catch(function () { }) } else e.target.pause() });
        }, { rootMargin: '200px' });
        vids.forEach(function (v) { io.observe(v) });
    } else vids.forEach(function (v) { v.autoplay = true; v.play() });

    var y = document.getElementById('year');
    if (y) y.textContent = new Date().getFullYear();
})();
