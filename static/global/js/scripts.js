const setTheme = (val) => {
    const theme = val ? val : localStorage.getItem('theme');
    const themeSwitcherInner = $('#theme-switcher-inner');
    const body = $('body');
    if (body.hasClass('dark') && theme !== 'dark') {
        body.removeClass('dark');
        themeSwitcherInner.removeClass('off');
    } else if (body.hasClass('light') && theme !== 'light') {
        body.removeClass('light');
        themeSwitcherInner.addClass('off');
    }
    body.addClass(theme);
};

$(function () {
    setTheme(localStorage.getItem('theme') || 'light');
    $('#mobile-menu').click(() => {
        $('#dd-menu').toggleClass('active');
    })
    $('#mobile-menu-close').click(() => {
        $('#dd-menu').removeClass('active');
    })
    $('#theme-switcher').click(() => {
        const themeSwitcherInner = $('#theme-switcher-inner');
        if (themeSwitcherInner.hasClass('off')) {
          themeSwitcherInner.removeClass('off');
          localStorage.setItem('theme', 'light');
          setTheme('light');
        } else {
          themeSwitcherInner.addClass('off');
          localStorage.setItem('theme', 'dark');
          setTheme('dark');
        }
    });
});