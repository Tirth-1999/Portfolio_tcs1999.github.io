/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*===== ACTIVE AND REMOVE MENU =====*/
const navLink = document.querySelectorAll('.nav__link');   

function linkAction(){
  /*Active link*/
  navLink.forEach(n => n.classList.remove('active'));
  this.classList.add('active');
  
  /*Remove menu mobile*/
  const navMenu = document.getElementById('nav-menu')
  navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction));

/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'bottom',
    distance: '50px',
    duration: 1000,
    reset: true
});

/*SCROLL HOME*/
sr.reveal('.home__title',{}); 
sr.reveal('.button',{delay: 200}); 
sr.reveal('.home__img',{delay: 400}); 
sr.reveal('.home__social-icon',{ interval: 200}); 

/*SCROLL ABOUT*/
sr.reveal('.about__img',{}); 
sr.reveal('.about__subtitle',{delay: 400}); 
sr.reveal('.about__text',{delay: 400}); 

/*SCROLL SKILLS*/
sr.reveal('.skills__subtitle',{}); 
sr.reveal('.skills__text',{}); 
sr.reveal('.skills__data',{interval: 200}); 
sr.reveal('.skills__img',{delay: 600});

/*SCROLL WORK*/
sr.reveal('.work__img',{}); 

/*SCROLL CONTACT*/
sr.reveal('.contact__input',{interval: 200}); 

const data = {
    labels: [
      'Co-Curricular',
      'Research',
      'Discipline',
      'Problem Solving',
      'Communication'
    ],
    datasets: [{
      label: 'Inculcated Skill',
      data: [80,85,85,95,90],
      backgroundColor: [
        'rgb(210,0,0,0.3)',
        'rgb(170,0,0,0.3)',
        'rgb(130,0,0,0.3)',
        'rgb(90,0,0,0.3)',
        'rgb(50,0,0,0.3)'],
      borderColor: [
        'rgba(0,0,0,0.5)',
        'rgba(0,0,0,0.5)',
        'rgba(0,0,0,0.5)',
        'rgba(0,0,0,0.5)',
        'rgba(0,0,0,0.5)'
    ],

    }]
  };
    // </block:setup>
    
    // <block:config:0>
        const config = {
            type: 'polarArea',
            data: data,

            options: {
              scales: {
                r: {
                  ticks: {
                    color: '#999999',
                    backdropColor : '#0f0f0f'
                  },
                  grid: {
                    color: 'rgb(0,0,0)',
                  }
                }
              }
            }
          };
    // </block:config>
    
    module.exports = {
    actions: [],
    config: config,
    };

