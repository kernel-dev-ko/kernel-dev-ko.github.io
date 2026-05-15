---
layout: home
permalink: /
title: "한국 리눅스 커널 개발자 모임"
description: "리눅스 커널에 관심을 가지고 연구/개발을 진행하고 있는 분들의 인적/기술적 교류 모임입니다."
---

{%- assign next_meetup = nil -%}
{%- for m in site.data.meetups -%}
  {%- if m.status == 'upcoming' and next_meetup == nil -%}
    {%- assign next_meetup = m -%}
  {%- endif -%}
{%- endfor -%}
{%- assign past_meetups = site.data.meetups | where: "status", "past" -%}
{%- assign news_sorted = site.data.news | sort: 'date' | reverse -%}
{%- assign latest_news = news_sorted | slice: 0, 3 -%}
{%- assign older_news  = news_sorted | slice: 3, 100 -%}

<!-- ============================ HERO ============================ -->
<section class="section section--hero" id="top" aria-labelledby="hero-title">
  <div class="container hero">
    <p class="hero__eyebrow">
      <span class="hero__prompt">$</span>
      <span>uname -a · Korea Linux Kernel Developers Meetup</span>
    </p>
    <h1 class="hero__title" id="hero-title">
      한국 리눅스 커널<br>개발자 모임
    </h1>
    <p class="hero__lede">
      리눅스 커널에 관심을 가지고 연구/개발을 진행하는 분들의
      인적·기술적 교류를 위한 비영리 커뮤니티입니다.
      한국에서 리눅스 커널에 관해 깊이 있게 논의할 자리를 다시 만들기 위해
      뜻을 모은 분들이 함께 운영합니다.
    </p>
    <div class="hero__cta">
      {%- if next_meetup -%}
        <a class="btn btn--primary" href="#next-meetup">다가오는 모임 보기</a>
      {%- endif -%}
      <a class="btn btn--ghost" href="{{ site.data.links.community[0].url }}">메일링 리스트 가입</a>
      <a class="btn btn--ghost" href="#past-meetups">지난 모임</a>
    </div>
    <dl class="hero__stats" aria-label="모임 현황">
      <div class="stat">
        <dt>누적 모임</dt>
        <dd>{{ site.data.meetups | size }}회</dd>
      </div>
      <div class="stat">
        <dt>운영 시작</dt>
        <dd>2017</dd>
      </div>
      <div class="stat">
        <dt>주요 채널</dt>
        <dd>Google Groups</dd>
      </div>
    </dl>
  </div>
</section>

<!-- ========================= NEXT MEETUP ======================== -->
{%- if next_meetup -%}
<section class="section" id="next-meetup" aria-labelledby="next-meetup-title">
  <div class="container">
    <header class="section__head">
      <p class="section__kicker">Next meetup</p>
      <h2 class="section__title" id="next-meetup-title">다가오는 모임</h2>
      <p class="section__sub">발표자와 주제가 확정되었습니다. 자리가 한정되어 있으니 사전에 참가 신청 부탁드립니다.</p>
    </header>

    <article class="meetup-card">
      <div class="meetup-card__head">
        <div>
          <p class="meetup-card__index">#{{ next_meetup.number | prepend: "0" | slice: -2, 2 }}</p>
          <h3 class="meetup-card__title">
            <a href="{{ next_meetup.slug | append: '/' | relative_url }}">{{ next_meetup.title }}</a>
          </h3>
        </div>
        <span class="badge badge--live">예정</span>
      </div>

      <dl class="meetup-card__meta">
        <div><dt>날짜</dt><dd><time datetime="{{ next_meetup.date | date: '%Y-%m-%d' }}">{{ next_meetup.date | date: "%Y년 %-m월 %-d일" }}</time></dd></div>
        {% if next_meetup.time %}<div><dt>시간</dt><dd>{{ next_meetup.time }}</dd></div>{% endif %}
        {% if next_meetup.venue %}<div><dt>장소</dt><dd>{{ next_meetup.venue }}</dd></div>{% endif %}
      </dl>

      <div class="meetup-card__actions">
        {% if next_meetup.rsvp %}<a class="btn btn--primary" href="{{ next_meetup.rsvp.url }}" rel="noopener">{{ next_meetup.rsvp.label }} →</a>{% endif %}
        <a class="btn btn--ghost" href="{{ next_meetup.slug | append: '/' | relative_url }}">전체 일정 보기</a>
        <a class="btn btn--ghost" href="{{ next_meetup.slug | append: '/presentation' | relative_url }}">발표자 모집 안내</a>
      </div>

      {% if next_meetup.sponsors %}
      <div class="meetup-card__sponsors">
        <p class="meetup-card__sponsors-label">후원</p>
        <ul class="sponsor-list">
          {% for s in next_meetup.sponsors %}
            <li><a href="{{ s.url }}" rel="noopener">{{ s.name }}</a><span class="sponsor-list__what"> · {{ s.contribution }}</span></li>
          {% endfor %}
        </ul>
      </div>
      {% endif %}
    </article>
  </div>
</section>
{%- endif -%}

<!-- ======================= COMMUNITY LINKS ====================== -->
<section class="section section--alt" id="community" aria-labelledby="community-title">
  <div class="container">
    <header class="section__head">
      <p class="section__kicker">Community</p>
      <h2 class="section__title" id="community-title">커뮤니티 채널</h2>
      <p class="section__sub">모임 공지와 자료가 공유되는 공식 채널입니다.</p>
    </header>

    <ul class="card-grid">
      {% for link in site.data.links.community %}
        <li>
          <a class="link-card link-card--{{ link.type }}" href="{{ link.url }}" rel="noopener">
            <p class="link-card__type">{{ link.name }}</p>
            <p class="link-card__handle">{{ link.handle }}</p>
            <p class="link-card__desc">{{ link.description }}</p>
            <span class="link-card__arrow" aria-hidden="true">→</span>
          </a>
        </li>
      {% endfor %}
    </ul>
  </div>
</section>

<!-- ========================= LATEST NEWS ======================== -->
<section class="section" id="news" aria-labelledby="news-title">
  <div class="container">
    <header class="section__head">
      <p class="section__kicker">News</p>
      <h2 class="section__title" id="news-title">새소식</h2>
      <p class="section__sub">최근 공지 위주로 보여드립니다. 더 이전 소식은 펼쳐서 확인할 수 있습니다.</p>
    </header>

    <ol class="news-list">
      {% for item in latest_news %}
        <li class="news-item">
          <time class="news-item__date" datetime="{{ item.date }}">{{ item.date | date: "%Y.%m.%d" }}</time>
          <div class="news-item__body">
            <h3 class="news-item__title">{{ item.title }}</h3>
            <div class="news-item__text">{{ item.body | markdownify }}</div>
            {% if item.link %}
              <a class="btn btn--small" href="{{ item.link.url }}" rel="noopener">{{ item.link.label }} →</a>
            {% endif %}
          </div>
        </li>
      {% endfor %}
    </ol>

    {% if older_news.size > 0 %}
    <details class="news-archive">
      <summary>지난 소식 {{ older_news.size }}건 더 보기</summary>
      <ol class="news-list news-list--compact">
        {% for item in older_news %}
          <li class="news-item">
            <time class="news-item__date" datetime="{{ item.date }}">{{ item.date | date: "%Y.%m.%d" }}</time>
            <div class="news-item__body">
              <h3 class="news-item__title">{{ item.title }}</h3>
              <div class="news-item__text">{{ item.body | markdownify }}</div>
            </div>
          </li>
        {% endfor %}
      </ol>
    </details>
    {% endif %}
  </div>
</section>

<!-- ========================= PAST MEETUPS ======================== -->
<section class="section section--alt" id="past-meetups" aria-labelledby="past-meetups-title">
  <div class="container">
    <header class="section__head">
      <p class="section__kicker">Archive</p>
      <h2 class="section__title" id="past-meetups-title">지난 모임</h2>
      <p class="section__sub">회차별 발표자료와 일정을 확인할 수 있습니다.</p>
    </header>

    <ol class="timeline" reversed>
      {% for m in past_meetups %}
        <li class="timeline__item">
          <span class="timeline__marker" aria-hidden="true"></span>
          <p class="timeline__date">
            {% if m.date_display %}{{ m.date_display }}{% else %}<time datetime="{{ m.date | date: '%Y-%m-%d' }}">{{ m.date | date: "%Y.%m.%d" }}</time>{% endif %}
          </p>
          <div class="timeline__body">
            <h3 class="timeline__title">
              {% if m.external %}
                <a href="{{ m.slug }}" rel="noopener">{{ m.title }} ↗</a>
              {% else %}
                <a href="{{ m.slug | append: '/' | relative_url }}">{{ m.title }}</a>
              {% endif %}
            </h3>
            {% if m.venue %}<p class="timeline__venue">{{ m.venue }}</p>{% endif %}
          </div>
          <span class="timeline__number">#{{ m.number | prepend: "0" | slice: -2, 2 }}</span>
        </li>
      {% endfor %}
    </ol>
  </div>
</section>

<!-- ============================ CONTACT ========================== -->
<section class="section" id="contact" aria-labelledby="contact-title">
  <div class="container">
    <header class="section__head">
      <p class="section__kicker">Contact</p>
      <h2 class="section__title" id="contact-title">의견 보내기</h2>
      <p class="section__sub">발표 제안, 후원, 공동 운영 문의 등 모든 의견을 환영합니다.</p>
    </header>

    <div class="contact-card">
      <p class="contact-card__label">이메일</p>
      <p class="contact-card__value">
        <a href="mailto:{{ site.data.links.contact.email }}">{{ site.data.links.contact.email }}</a>
      </p>
      <p class="contact-card__hint">
        보내주신 메일은 운영진이 확인 후 답신드립니다.
        모든 공식 공지는 <a href="{{ site.data.links.community[0].url }}" rel="noopener">메일링 리스트</a>로 가장 먼저 발송됩니다.
      </p>
    </div>
  </div>
</section>
