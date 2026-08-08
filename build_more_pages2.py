import sys
sys.path.insert(0, '.')
from generate_page import render_page

def crumb(title):
    return f'''<nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <span aria-current="page">{title}</span>
      </nav>'''


# ============================================================
# /reviews/
# ============================================================
reviews_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Відгуки")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Відгуки</p>
        <h1 data-reveal data-reveal-delay="1">Слова пацієнтів</h1>
        <p data-reveal data-reveal-delay="2">Середня оцінка 5.0 на основі 184 відгуків у Google та Doc.ua.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reviews" data-reviews data-reveal>
        <div class="reviews-track" data-reviews-track tabindex="0" role="group" aria-label="Відгуки пацієнтів, гортайте свайпом або стрілками">
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Обирала клініку довго й прискіпливо. ST — це рівень, який одразу відчувається: від першого дзвінка до фінального результату. Жодного відчуття конвеєра.</blockquote>
            <div class="review-person">
              <img src="../images/patient-nataliia.png" width="200" height="200" alt="Портрет пацієнтки Наталії К." loading="lazy" decoding="async">
              <div><p class="rname">Наталія К.</p><p class="rmeta">Вініри, 8 одиниць</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Імплантацію відкладав роками через страх. У ST усе пояснили заздалегідь, показали 3D-план — і процедура пройшла спокійно, без сюрпризів.</blockquote>
            <div class="review-person">
              <img src="../images/patient-dmytro.png" width="200" height="200" alt="Портрет пацієнта Дмитра С." loading="lazy" decoding="async">
              <div><p class="rname">Дмитро С.</p><p class="rmeta">Імплантація Nobel Biocare</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Дизайн усмішки, який мені показали до лікування, збігся з результатом майже ідеально. Це той рівень точності, за який справді хочеться платити.</blockquote>
            <div class="review-person">
              <img src="../images/patient-iryna.png" width="200" height="200" alt="Портрет пацієнтки Ірини П." loading="lazy" decoding="async">
              <div><p class="rname">Ірина П.</p><p class="rmeta">Дизайн усмішки</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Привела дитину на профілактику й залишилася сама як пацієнт. Тут не продають зайвого — навпаки, відмовили від процедури, яку радили в іншій клініці.</blockquote>
            <div class="review-person">
              <img src="../images/patient-oksana.png" width="200" height="200" alt="Портрет пацієнтки Оксани Л." loading="lazy" decoding="async">
              <div><p class="rname">Оксана Л.</p><p class="rmeta">Терапія, гігієна</p></div>
            </div>
          </article>
        </div>

        <div class="reviews-controls">
          <div class="reviews-dots" data-reviews-dots role="tablist" aria-label="Навігація по відгуках"></div>
          <div class="gallery-arrows">
            <button type="button" aria-label="Попередній відгук" data-reviews-prev><svg aria-hidden="true"><use href="#icon-chevron-left"></use></svg></button>
            <button type="button" aria-label="Наступний відгук" data-reviews-next><svg aria-hidden="true"><use href="#icon-chevron-right"></use></svg></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете стати нашим наступним відгуком?</h3>
          <p>Консультація хірурга безкоштовна — почніть зі знайомства.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="reviews/index.html",
    title="Відгуки пацієнтів ST Стоматологія | Київ",
    description="184 відгуки пацієнтів ST Стоматологія із середньою оцінкою 5.0. Реальні історії лікування — вініри, імплантація, дизайн усмішки.",
    canonical_path="/reviews/",
    active_href="/reviews/",
    main_html=reviews_main,
    depth=1,
)


# ============================================================
# /faq/
# ============================================================
faq_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Питання")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Питання</p>
        <h1 data-reveal data-reveal-delay="1">Що запитують найчастіше</h1>
        <p data-reveal data-reveal-delay="2">Не знайшли відповідь? Напишіть напряму — адміністратор відповість протягом 15 хвилин у робочі години.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div class="faq-list" data-reveal>
        <details class="acc" open>
          <summary><span class="acc-title">Чи боляче встановлювати вініри?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні. Препарування проходить під локальною анестезією і зачіпає мінімальний шар емалі — 0,3–0,5 мм. Більшість пацієнтів описує відчуття як тиск, а не біль. Між візитами ви носите тимчасові накладки, тож дискомфорту в побуті немає.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки триває імплантація?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Хірургічний етап займає 40–60 хвилин на одну одиницю — це один візит. Далі йде остеоінтеграція: від 3 до 5 місяців залежно від щелепи та щільності кістки. Після цього встановлюємо коронку за 2 візити.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи є розсрочка або оплата частинами?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так. Для лікування вартістю від 30 000 ₴ доступна безвідсоткова розсрочка до 12 місяців. Довідки про доходи не потрібні, оформлення відбувається на першому візиті й займає близько 15 хвилин.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Що входить у першу консультацію?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Огляд, фотопротокол, обговорення очікуваного результату та письмовий план лікування з кошторисом. Консультація хірурга-імплантолога — безкоштовна. 3D-томографія за потреби оплачується окремо (1 100 ₴).</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки служать вініри та імпланти?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Кераміка E.max за коректної гігієни служить 15–20 років, наша гарантія — 7 років. Імпланти Nobel Biocare мають довічну гарантію виробника; коронка на імпланті — гарантія 5 років.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи можна лікуватися під час вагітності?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так, терапія та гігієна безпечні у другому триместрі — ми використовуємо анестетики без адреналіну. Хірургічні втручання, відбілювання та планові рентген-обстеження переносимо на період після народження дитини.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Лишилися питання?</h3>
          <p>Зателефонуйте або запишіться на безкоштовну консультацію — відповімо на все особисто.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="faq/index.html",
    title="Питання й відповіді про лікування | ST Стоматологія",
    description="Відповіді на часті питання про вініри, імплантацію, розстрочку та консультацію в ST Стоматологія, Київ.",
    canonical_path="/faq/",
    active_href="/faq/",
    main_html=faq_main,
    depth=1,
)


# ============================================================
# /results/  (до/після)
# ============================================================
results_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Результати")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Результати</p>
        <h1 data-reveal data-reveal-delay="1">До і після</h1>
        <p data-reveal data-reveal-delay="2">Перетягніть повзунок, щоб побачити трансформацію. Реальні клінічні випадки пацієнтів ST.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="ba-wrap">
        <figure class="ba-case" data-reveal>
          <div class="ba-slider" style="--ba-pos:50%" data-ba>
            <img class="ba-before" src="../images/case-1-before.jpg" width="1000" height="474" alt="Стан зубного ряду пацієнта до комплексної реставрації" loading="lazy" decoding="async">
            <img class="ba-after" src="../images/case-1-after.jpg" width="1000" height="489" alt="Стан зубного ряду пацієнта після комплексної реставрації" loading="lazy" decoding="async">
            <span class="ba-tag before">До</span>
            <span class="ba-tag after">Після</span>
            <div class="ba-handle" aria-hidden="true"><span class="ba-handle-grip"><svg><use href="#icon-drag"></use></svg></span></div>
            <input type="range" min="0" max="100" value="50" step="0.1" class="ba-range" aria-label="Повзунок порівняння до і після, комплексна реставрація">
          </div>
          <figcaption class="ba-caption"><strong>Комплексна реставрація зубного ряду</strong>Реальний клінічний випадок пацієнта.</figcaption>
        </figure>

        <figure class="ba-case" data-reveal data-reveal-delay="1">
          <div class="ba-slider" style="--ba-pos:50%" data-ba>
            <img class="ba-before" src="../images/case-2-before.png" width="900" height="700" alt="Стан прикусу пацієнта до імплантації у клініці ST" loading="lazy" decoding="async">
            <img class="ba-after" src="../images/case-2-after.png" width="900" height="700" alt="Стан прикусу пацієнта після імплантації у клініці ST" loading="lazy" decoding="async">
            <span class="ba-tag before">До</span>
            <span class="ba-tag after">Після</span>
            <div class="ba-handle" aria-hidden="true"><span class="ba-handle-grip"><svg><use href="#icon-drag"></use></svg></span></div>
            <input type="range" min="0" max="100" value="50" step="0.1" class="ba-range" aria-label="Повзунок порівняння до і після, імплантація">
          </div>
          <figcaption class="ba-caption"><strong>Імплантація Nobel Biocare</strong>Відновлення двох одиниць у бічній ділянці.</figcaption>
        </figure>
      </div>
      <p class="form-fine" style="margin-top:2rem">Фото використані за згодою пацієнтів. Результат індивідуальний і залежить від вихідного стану.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете такий самий результат?</h3>
          <p>Консультація хірурга безкоштовна — обговоримо ваш випадок і покажемо орієнтовний план.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="results/index.html",
    title="До і після — реальні результати лікування | ST Стоматологія",
    description="Реальні клінічні випадки пацієнтів ST Стоматологія: комплексна реставрація зубного ряду, імплантація Nobel Biocare. Порівняйте до і після.",
    canonical_path="/results/",
    active_href="/results/",
    main_html=results_main,
    depth=1,
)


# ============================================================
# /contact/
# ============================================================
contact_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Контакти")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Контакти</p>
        <h1 data-reveal data-reveal-delay="1">Як нас знайти</h1>
        <p data-reveal data-reveal-delay="2">Приходьте на консультацію або зателефонуйте — відповімо на всі питання й підберемо зручний час.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div class="contact-info" data-reveal>
          <div class="contact-block">
            <h4>Адреса</h4>
            <p>вул. Хрещатик, 15, Київ</p>
            <p class="fine">3 хвилини пішки від станції метро «Хрещатик»</p>
          </div>
          <div class="contact-block">
            <h4>Телефон</h4>
            <a href="tel:+380441234567">+380 44 123 45 67</a>
          </div>
          <div class="contact-block">
            <h4>Пошта</h4>
            <a href="mailto:hello@st-dental.ua">hello@st-dental.ua</a>
          </div>
          <div class="contact-block">
            <h4>Години роботи</h4>
            <p class="fine">Пн–Пт: 09:00 — 20:00</p>
            <p class="fine">Сб: 10:00 — 17:00</p>
            <p class="fine">Нд: вихідний</p>
          </div>
        </div>

        <div class="map-frame" data-reveal data-reveal-delay="1">
          <iframe
            src="https://www.google.com/maps?q=Khreshchatyk%2015%2C%20Kyiv&output=embed"
            title="Карта розташування клініки ST на вулиці Хрещатик, Київ"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            aria-label="Інтерактивна карта з розташуванням клініки ST">
          </iframe>
        </div>
      </div>

      <div class="cta-banner" data-reveal style="margin-top:3rem">
        <div>
          <h3>Простіше записатися онлайн</h3>
          <p>Заповніть коротку форму — адміністратор передзвонить протягом 15 хвилин.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="contact/index.html",
    title="Контакти ST Стоматологія | Адреса, телефон, години роботи",
    description="ST Стоматологія: вул. Хрещатик, 15, Київ. Телефон +380 44 123 45 67. Графік роботи, карта проїзду, онлайн-запис.",
    canonical_path="/contact/",
    active_href="/contact/",
    main_html=contact_main,
    depth=1,
)
