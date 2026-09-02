document.addEventListener('DOMContentLoaded', () => {
  // Botão Voltar ao Topo
  const backToTopBtn = document.getElementById('btn-back-to-top');
  
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Ano Dinâmico no Footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Marcação de Menu Ativo
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-list a');
  navLinks.forEach(link => {
    // Pegar apenas o nome do arquivo para comparar (ex: sobre-nos.html)
    const linkPath = link.getAttribute('href');
    // Marca como ativo se o href do link for igual ao path atual (evitar marcar a Home sempre)
    if (currentPath.includes(linkPath) && linkPath !== 'index.html' && linkPath !== '/') {
      link.classList.add('active');
    }
  }); // <-- Added missing closing brace for forEach

  // Menu Hambúrguer Mobile (Injeção Dinâmica para todas as páginas)
  const nav = document.querySelector('.nav');
  const navList = document.querySelector('.nav-list');
  const headerActions = document.querySelector('.header-actions');
  
  if (nav && navList && !document.querySelector('.mobile-menu-toggle')) {
    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'mobile-menu-toggle';
    toggleBtn.innerHTML = '☰';
    toggleBtn.setAttribute('aria-label', 'Abrir menu de navegação');
    nav.insertBefore(toggleBtn, navList);

    // Injetar os 2 botões de Portal dentro do menu hambúrguer no mobile (Padrão Razonet)
    if (headerActions && !navList.querySelector('.mobile-portal-item')) {
      const portalLi = document.createElement('li');
      portalLi.className = 'mobile-portal-item';
      portalLi.style.cssText = 'display: flex; flex-direction: column; gap: 0.6rem; padding: 1.2rem 1rem 0.5rem 1rem; border-top: 1px solid #E5E7EB; margin-top: 0.8rem; width: 100%;';
      
      const btnCliente = document.createElement('a');
      btnCliente.href = 'https://onvio.com.br/clientcenter/pt/auth?r=%2Fhome';
      btnCliente.target = '_blank';
      btnCliente.rel = 'noopener noreferrer';
      btnCliente.className = 'btn-primary';
      btnCliente.style.cssText = 'padding: 0.7rem 1rem; font-size: 0.95rem; text-align: center; width: 100%; display: block; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);';
      btnCliente.textContent = 'Portal do Cliente';

      const btnEmpregado = document.createElement('a');
      btnEmpregado.href = 'https://onvio.com.br/login/#/';
      btnEmpregado.target = '_blank';
      btnEmpregado.rel = 'noopener noreferrer';
      btnEmpregado.className = 'btn-secondary';
      btnEmpregado.style.cssText = 'padding: 0.7rem 1rem; font-size: 0.95rem; text-align: center; width: 100%; display: block; border-radius: 8px; color: var(--primary-color); border: 2px solid var(--primary-color); background: transparent; font-weight: 600;';
      btnEmpregado.textContent = 'Portal do Empregado';

      portalLi.appendChild(btnCliente);
      portalLi.appendChild(btnEmpregado);
      navList.appendChild(portalLi);
    }

    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      navList.classList.toggle('active');
      toggleBtn.innerHTML = navList.classList.contains('active') ? '✕' : '☰';
    });

    // Fechar menu ao clicar fora
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target)) {
        navList.classList.remove('active');
        toggleBtn.innerHTML = '☰';
      }
    });

    // Fechar menu ao clicar em links (exceto dropdown que só abre sub-menu no mobile)
    navList.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', (e) => {
        if (link.parentElement.classList.contains('dropdown') && window.innerWidth <= 768) {
          e.preventDefault();
          link.parentElement.classList.toggle('active');
        } else if (window.innerWidth <= 768) {
          navList.classList.remove('active');
          toggleBtn.innerHTML = '☰';
        }
      });
    });
  }

  // Cálculo de Anos de Experiência Dinâmico (Fundação em 2009)
  const anoFundacao = 2009;
  const anosExperiencia = new Date().getFullYear() - anoFundacao;
  const elementosAnos = document.querySelectorAll('.anos-experiencia');
  elementosAnos.forEach(el => {
    el.textContent = anosExperiencia;
  });

});

// Lógica Global dos Modais
const modalOptions = {
  'para-voce': ['Imposto de Renda', 'Empregado Doméstico', 'Autônomo', 'Outros'],
  'abra-empresa': ['Quero ser MEI', 'Sou MEI', 'Quero Migrar para Simples Nacional', 'Prestação de Serviços', 'Comércio', 'Indústria', 'Outros'],
  'troque-contador': ['Sou MEI', 'Quero Migrar para Simples Nacional', 'Prestação de Serviços', 'Comércio', 'Indústria', 'Outros']
};

window.abrirModal = function(tipo) {
  const overlay = document.getElementById('modal-overlay');
  const modal = document.getElementById('modal-form');
  const select = document.getElementById('modal-selecao');
  
  if (overlay && modal && select) {
    // Limpar opções anteriores
    select.innerHTML = '<option value="">Selecione</option>';
    
    // Injetar novas opções
    if (modalOptions[tipo]) {
      modalOptions[tipo].forEach(opcao => {
        const opt = document.createElement('option');
        opt.value = opcao;
        opt.textContent = opcao;
        select.appendChild(opt);
      });
    }
    
    // Mostrar modal
    overlay.classList.add('visible');
    modal.classList.add('visible');
    document.body.style.overflow = 'hidden'; // Previne scroll da página de fundo
  }
};

window.fecharModal = function() {
  const overlay = document.getElementById('modal-overlay');
  const modal = document.getElementById('modal-form');
  if (overlay && modal) {
    overlay.classList.remove('visible');
    modal.classList.remove('visible');
    document.body.style.overflow = 'auto'; // Restaura scroll
  }
};

// --- YouTube Feed Fetcher ---
// Busca os 3 últimos vídeos do canal fornecido via RSS2JSON
document.addEventListener('DOMContentLoaded', () => {
  const youtubeContainer = document.getElementById('youtube-feed');
  if (!youtubeContainer) return;

  const CHANNEL_ID = 'UCCtGiaBa4DCWaNs2ei8c09g';
  const RSS_URL = encodeURIComponent(`https://www.youtube.com/feeds/videos.xml?channel_id=${CHANNEL_ID}`);
  const API_URL = `https://api.rss2json.com/v1/api.json?rss_url=${RSS_URL}`;

  fetch(API_URL)
    .then(response => response.json())
    .then(data => {
      const renderFallback = () => {
        youtubeContainer.innerHTML = '';
        const fallbackVideo = {
          link: 'https://www.youtube.com/@contabilidadecamilo',
          thumbnail: 'https://img.youtube.com/vi/mD6Zht09EiA/hqdefault.jpg',
          title: 'Acesse nosso canal para mais dicas de Contabilidade e Negócios!'
        };
        
        const iframeHtml = `
          <a href="${fallbackVideo.link}" target="_blank" rel="noopener noreferrer" style="display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
            <div style="width: 100%; aspect-ratio: 16/9; background-image: url('${fallbackVideo.thumbnail}'); background-size: cover; background-position: center; position: relative;">
              <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="white" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-play" style="opacity: 0.9;"><polygon points="6 3 20 12 6 21 6 3"/></svg>
              </div>
            </div>
            <div style="padding: 1rem; background: white;">
              <h4 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">${fallbackVideo.title}</h4>
            </div>
          </a>
        `;
        youtubeContainer.insertAdjacentHTML('beforeend', iframeHtml);
      };

      if (data.status === 'ok' && data.items.length > 0) {
        youtubeContainer.innerHTML = ''; // Limpa o "Carregando..."
        
        // Pega apenas os 3 primeiros vídeos
        const latestVideos = data.items.slice(0, 3);
        
        latestVideos.forEach(video => {
          // Extrai o ID do vídeo com segurança usando o guid (ex: "yt:video:mD6Zht09EiA")
          const videoId = video.guid.split(':')[2];
          
          const iframeHtml = `
            <a href="${video.link}" target="_blank" rel="noopener noreferrer" style="display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
              <div style="width: 100%; aspect-ratio: 16/9; background-image: url('${video.thumbnail}'); background-size: cover; background-position: center; position: relative;">
                <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="white" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-play" style="opacity: 0.9;"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
              </div>
              <div style="padding: 1rem; background: white;">
                <h4 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">${video.title}</h4>
              </div>
            </a>
          `;
          youtubeContainer.insertAdjacentHTML('beforeend', iframeHtml);
        });
      } else {
        renderFallback();
      }
    })
    .catch(error => {
      console.error('Erro ao buscar vídeos do YouTube:', error);
      // Se a API falhar completamente (404/500/CORS), usamos o fallback visual
      const youtubeContainer = document.getElementById('youtube-feed');
      youtubeContainer.innerHTML = '';
      const fallbackVideo = {
        link: 'https://www.youtube.com/@contabilidadecamilo',
        thumbnail: 'https://img.youtube.com/vi/mD6Zht09EiA/hqdefault.jpg',
        title: 'Acesse nosso canal para mais dicas de Contabilidade e Negócios!'
      };
      const iframeHtml = `
        <a href="${fallbackVideo.link}" target="_blank" rel="noopener noreferrer" style="display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-decoration: none; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
          <div style="width: 100%; aspect-ratio: 16/9; background-image: url('${fallbackVideo.thumbnail}'); background-size: cover; background-position: center; position: relative;">
            <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center;">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="white" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-play" style="opacity: 0.9;"><polygon points="6 3 20 12 6 21 6 3"/></svg>
            </div>
          </div>
          <div style="padding: 1rem; background: white;">
            <h4 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">${fallbackVideo.title}</h4>
          </div>
        </a>
      `;
      youtubeContainer.insertAdjacentHTML('beforeend', iframeHtml);
    });
});

// Accordion Logic
document.addEventListener('DOMContentLoaded', () => {
  const accordionItems = document.querySelectorAll('.accordion-item');
  
  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    
    // Add the trigger text dynamically after summary
    const summary = item.querySelector('.accordion-summary-text');
    const trigger = document.createElement('div');
    trigger.className = 'btn-toggle-text';
    trigger.innerHTML = 'Clique para ver o guia completo &darr;';
    
    // Insert trigger after summary
    if(summary) {
      summary.insertAdjacentElement('afterend', trigger);
    }
    
    const toggleAccordion = () => {
      const isActive = item.classList.contains('active');
      
      // Close all others
      accordionItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        const otherTrigger = otherItem.querySelector('.btn-toggle-text');
        if(otherTrigger) otherTrigger.innerHTML = 'Clique para ver o guia completo &darr;';
      });
      
      if (!isActive) {
        item.classList.add('active');
        if(trigger) trigger.innerHTML = 'Clique para fechar &uarr;';
      }
    };
    
    header.addEventListener('click', toggleAccordion);
    if(trigger) {
      trigger.addEventListener('click', toggleAccordion);
    }
  });
  
  // WhatsApp form redirect
  const diagForm = document.getElementById('diagnostico-form');
  if(diagForm) {
    diagForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const nome = document.getElementById('diag-nome').value;
      const cnpj = document.getElementById('diag-cnpj').value;
      const regime = document.getElementById('diag-regime').value;
      const zap = document.getElementById('diag-whatsapp').value;
      
      const mensagem = `Olá! Gostaria de solicitar um Diagnóstico Fiscal gratuito.%0A%0A*Nome:* ${nome}%0A*CNPJ:* ${cnpj}%0A*Regime Atual:* ${regime}%0A*Meu WhatsApp:* ${zap}`;
      
      const url = `https://wa.me/5511944913323?text=${mensagem}`;
      window.open(url, '_blank');
    });
  }
});


// Tema Escuro (Dark Mode Toggle)
const initThemeToggle = () => {
  const nav = document.querySelector('.nav');
  if (!nav) return;

  if (document.querySelector('.theme-toggle-btn')) return;

  const themeBtn = document.createElement('button');
  themeBtn.className = 'theme-toggle-btn';
  themeBtn.setAttribute('aria-label', 'Alternar tema');
  
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  themeBtn.innerHTML = isDark ? '☀' : '☾';
  themeBtn.style.marginRight = '1rem'; // Espaço antes dos botões de ação

  const navList = document.querySelector('.nav-list');
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  
  if (mobileToggle) {
    nav.insertBefore(themeBtn, mobileToggle);
  } else if (navList) {
    nav.appendChild(themeBtn);
  } else {
    nav.appendChild(themeBtn);
  }

  themeBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    if (newTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        document.documentElement.removeAttribute('data-theme');
    }
    localStorage.setItem('theme', newTheme);
    
    themeBtn.innerHTML = newTheme === 'dark' ? '☀' : '☾';
  });
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initThemeToggle);
} else {
  initThemeToggle();
}
