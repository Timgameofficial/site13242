import sys
sys.path.insert(0, '.')
from generate_page import render_page

# ============================================================
# /services/  — хаб-сторінка з переліком усіх послуг
# ============================================================
services_main = '''
  <section class="page-hero">
    <div class="container">
      <nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <span aria-current="page">Послуги</span>
      </nav>
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Послуги</p>
        <h1 data-reveal data-reveal-delay="1">Три напрями досконалості</h1>
        <p data-reveal data-reveal-delay="2">Ми свідомо не розпорошуємось. Натомість — глибина в трьох напрямах, де ST задає стандарт: естетична реставрація, хірургічна імплантологія та цифровий дизайн усмішки.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="services-grid">
        <article class="service-card" data-reveal>
          <svg class="service-icon" aria-hidden="true"><use href="#icon-veneer"></use></svg>
          <h3>Преміум вініри</h3>
          <p>Керамічні реставрації E.max, виготовлені індивідуально під анатомію та тон емалі. Мінімальне препарування, максимальна природність.</p>
          <ul class="service-list">
            <li>Мінімальна обробка емалі</li>
            <li>Гарантія 7 років</li>
            <li>Строк — 2 візити</li>
          </ul>
          <a href="/services/veneers/" class="service-link">Детальніше про вініри <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
        </article>
        <article class="service-card" data-reveal data-reveal-delay="1">
          <svg class="service-icon" aria-hidden="true"><use href="#icon-implant"></use></svg>
          <h3>Цифрова імплантологія</h3>
          <p>Імплантація системами Nobel Biocare з хірургічним шаблоном за даними 3D-томографії. Точність до десятої частки міліметра.</p>
          <ul class="service-list">
            <li>Хірургічний шаблон</li>
            <li>Довічна гарантія на імплант</li>
            <li>Без розрізу в 70% випадків</li>
          </ul>
          <a href="/services/implants/" class="service-link">Детальніше про імплантацію <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
        </article>
        <article class="service-card" data-reveal data-reveal-delay="2">
          <svg class="service-icon" aria-hidden="true"><use href="#icon-smile"></use></svg>
          <h3>Дизайн усмішки</h3>
          <p>Цифрове моделювання майбутньої усмішки ще до початку лікування. Ви бачите результат — і затверджуєте його — заздалегідь.</p>
          <ul class="service-list">
            <li>3D-прев'ю результату</li>
            <li>Примірка mock-up</li>
            <li>Затвердження до старту</li>
          </ul>
          <a href="/services/smile-design/" class="service-link">Детальніше про дизайн усмішки <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Не впевнені, що саме потрібно?</h3>
          <p>Консультація хірурга безкоштовна — визначимо оптимальний план разом.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="services/index.html",
    title="Послуги — вініри, імплантація, дизайн усмішки | ST Стоматологія",
    description="Три напрями ST Стоматологія: преміум вініри E.max, цифрова імплантологія Nobel Biocare, дизайн усмішки. Ціни та деталі кожної послуги.",
    canonical_path="/services/",
    active_href="/services/",
    main_html=services_main,
    depth=1,
)


# ============================================================
# /prices/  — повний прайс окремою сторінкою
# ============================================================
prices_main = '''
  <section class="page-hero">
    <div class="container">
      <nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <span aria-current="page">Ціни</span>
      </nav>
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Вартість</p>
        <h1 data-reveal data-reveal-delay="1">Меню послуг</h1>
        <p data-reveal data-reveal-delay="2">Прозорі ціни без прихованих доплат. Фінальна вартість затверджується після діагностики та письмово фіксується в плані лікування.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Естетична стоматологія</span>
            <span class="acc-meta">4 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Вінір E.max</span><span class="leader"></span><span class="price">від 18 500 ₴</span></div>
              <span class="desc">за одиницю, кераміка пресована · <a href="/services/veneers/">детальніше</a></span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Художня реставрація</span><span class="leader"></span><span class="price">від 3 400 ₴</span></div>
              <span class="desc">композитна, 1 зуб</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Професійна гігієна</span><span class="leader"></span><span class="price">2 200 ₴</span></div>
              <span class="desc">Air Flow + ультразвук</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Цифровий дизайн усмішки</span><span class="leader"></span><span class="price">6 800 ₴</span></div>
              <span class="desc">3D-моделювання результату · <a href="/services/smile-design/">детальніше</a></span>
            </div>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-title">Імплантологія та хірургія</span>
            <span class="acc-meta">4 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Імплант Nobel Biocare</span><span class="leader"></span><span class="price">від 34 900 ₴</span></div>
              <span class="desc">імплант + хірургічний етап · <a href="/services/implants/">детальніше</a></span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">3D-томографія</span><span class="leader"></span><span class="price">1 100 ₴</span></div>
              <span class="desc">повна щелепа</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Хірургічний шаблон</span><span class="leader"></span><span class="price">4 200 ₴</span></div>
              <span class="desc">індивідуальний друк за даними КТ</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Коронка на імпланті</span><span class="leader"></span><span class="price">від 16 000 ₴</span></div>
              <span class="desc">кераміка, індивідуальний абатмент</span>
            </div>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-title">Терапія та гігієна</span>
            <span class="acc-meta">3 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Лікування карієсу</span><span class="leader"></span><span class="price">від 2 100 ₴</span></div>
              <span class="desc">1 канал/поверхня, під мікроскопом</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Ендодонтичне лікування</span><span class="leader"></span><span class="price">від 4 800 ₴</span></div>
              <span class="desc">1 канал, під мікроскопом</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Консультація терапевта</span><span class="leader"></span><span class="price">безкоштовно</span></div>
              <span class="desc">з фотопротоколом</span>
            </div>
          </div>
        </details>
      </div>
      <p class="form-fine" style="margin-top:1.5rem">Ціни орієнтовні й не є публічною офертою. Точну вартість ви отримаєте письмово після діагностики.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете точний кошторис?</h3>
          <p>Запишіться на безкоштовну консультацію — отримаєте план лікування з цінами того ж дня.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="prices/index.html",
    title="Ціни на стоматологічні послуги | ST Стоматологія",
    description="Повний прайс ST Стоматологія: вініри, імплантація, терапія та гігієна. Прозорі ціни без прихованих доплат.",
    canonical_path="/prices/",
    active_href="/prices/",
    main_html=prices_main,
    depth=1,
)


# ============================================================
# /team/  — команда лікарів
# ============================================================
team_main = '''
  <section class="page-hero">
    <div class="container">
      <nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <span aria-current="page">Команда</span>
      </nav>
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Команда</p>
        <h1 data-reveal data-reveal-delay="1">Лікарі, яким довіряють</h1>
        <p data-reveal data-reveal-delay="2">Троє фахівців, чия практика формує стандарт студії ST — кожен веде свій напрям від першої консультації до фінального результату.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="team-grid">
        <article class="team-card" data-reveal>
          <div class="team-frame">
            <img src="../images/doctor-olena.png" width="600" height="600" alt="Олена Крамар — лікар-стоматолог ST, спеціаліст з естетичної реставрації" loading="lazy" decoding="async">
            <div class="team-badge"><span class="yrs">18</span><span class="txt">років</span></div>
          </div>
          <h3>Олена Крамар</h3>
          <p class="team-role">Естетична стоматологія</p>
          <p>Спеціалізується на вінірах та мікропротезуванні. Понад 400 успішних кейсів естетичної реставрації. Веде напрям <a href="/services/veneers/">преміум вінірів</a>.</p>
        </article>
        <article class="team-card" data-reveal data-reveal-delay="1">
          <div class="team-frame">
            <img src="../images/doctor-andrii.png" width="600" height="600" alt="Андрій Тарасенко — лікар-хірург-імплантолог ST" loading="lazy" decoding="async">
            <div class="team-badge"><span class="yrs">22</span><span class="txt">роки</span></div>
          </div>
          <h3>Андрій Тарасенко</h3>
          <p class="team-role">Хірургія та імплантологія</p>
          <p>Сертифікований спеціаліст Nobel Biocare. Проводить складні випадки повної реабілітації прикусу. Веде напрям <a href="/services/implants/">імплантології</a>.</p>
        </article>
        <article class="team-card" data-reveal data-reveal-delay="2">
          <div class="team-frame">
            <img src="../images/doctor-mariia.png" width="600" height="600" alt="Марія Войтенко — лікар-ортодонт ST" loading="lazy" decoding="async">
            <div class="team-badge"><span class="yrs">14</span><span class="txt">років</span></div>
          </div>
          <h3>Марія Войтенко</h3>
          <p class="team-role">Ортодонтія та дизайн усмішки</p>
          <p>Веде цифрове планування усмішки. Автор індивідуального протоколу передбачуваного результату ST. Веде напрям <a href="/services/smile-design/">дизайну усмішки</a>.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Готові познайомитися особисто?</h3>
          <p>Перша консультація — безкоштовна, без зобов'язань.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="team/index.html",
    title="Команда лікарів ST Стоматологія | Київ",
    description="Троє лікарів ST Стоматологія: естетична реставрація, хірургічна імплантологія, ортодонтія та дизайн усмішки. Досвід від 14 до 22 років.",
    canonical_path="/team/",
    active_href="/team/",
    main_html=team_main,
    depth=1,
)
