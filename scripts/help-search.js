!function(){"use strict";var pop=document.getElementById("siteMenu"),form=document.getElementById("helpSearchForm"),input=document.getElementById("helpSearchInput"),list=document.getElementById("helpRecentList"),title=document.getElementById("helpRecentTitle");if(pop&&form&&input&&list){var open,KEY="fs-help-recents",HELP_URL=(open=pop.querySelector("a.help-menu-open"))?open.getAttribute("href"):"help.html",SUGGESTED=[{t:"Getting Started",q:"getting started"},{t:"Connecting a Channel",q:"connecting a channel"},{t:"Recurring Messages",q:"recurring messages"},{t:"Premium & Billing",q:"premium billing"},{t:"Media & Photo Posts",q:"photo video posts"},{t:"Fix: Post Not Sent",q:"post not sent"},{t:"Edit or Delete a Post",q:"edit delete scheduled"}];new MutationObserver(function(){pop.classList.contains("open")&&render()}).observe(pop,{attributes:!0,attributeFilter:["class"]}),form.addEventListener("submit",function(e){e.preventDefault();var q=input.value.trim();if(q){try{var rec=readRecents().filter(function(x){return x!==q});rec.unshift(q),localStorage.setItem(KEY,JSON.stringify(rec.slice(0,6)))}catch(err){}window.open(HELP_URL+"#/s/"+encodeURIComponent(q),"_blank","noopener")}})}function readRecents(){try{return JSON.parse(localStorage.getItem(KEY)||"[]")}catch(e){return[]}}function render(){var rec=readRecents().slice(0,5);list.textContent="",rec.length?(title.textContent="Recent searches",rec.forEach(function(q){var a=document.createElement("a");a.href=HELP_URL+"#/s/"+encodeURIComponent(q),a.textContent=q,list.appendChild(a)})):(title.textContent="Popular articles",function(arr,n){for(var a=arr.slice(),i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j],a[j]=t}return a.slice(0,n)}(SUGGESTED,3).forEach(function(s){var a=document.createElement("a");a.href=HELP_URL+"#/s/"+encodeURIComponent(s.q),a.textContent=s.t,list.appendChild(a)}))}}();/* Mobile header search affordance (Oct 2026). Every published page loads this
   file, so the icon is injected once here: help pages trade their Open-Bot
   header button for it, blog pages gain a shortcut to the blog search box. */
(function(){"use strict";
  if(!window.matchMedia||!matchMedia("(max-width: 860px)").matches)return;
  var header=document.querySelector("header.site .nav")||document.querySelector("header.site");
  if(!header||header.querySelector(".nav-search-m"))return;
  var path=location.pathname,isBlog=/\/blog\//.test(path),isHelp=!isBlog&&/\/help(\.html|\/)/.test(path);
  var inArticle=/\/blog\/a\//.test(path),href=inArticle?"../index.html?focus=1":null;
  var btn=document.createElement(href?"a":"button");
  btn.className="icon-btn nav-search-m";
  if(href)btn.setAttribute("href",href);else btn.setAttribute("type","button");
  btn.setAttribute("aria-label",isBlog?"Search articles":"Search help");
  btn.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
  function box(){return document.getElementById("blog-q")||document.getElementById("helpSearchInput")||document.querySelector(".hc-hsearch input")||document.getElementById("hcSearch")||document.getElementById("hcq")}
  btn.addEventListener("click",function(e){if(href)return;e.preventDefault();var b=box();if(b){try{b.focus();b.scrollIntoView({block:"center",behavior:"smooth"})}catch(err){try{b.focus()}catch(e2){}}}else location.href="help.html?focus=1"});
  var anchor=header.querySelector(".settings-wrap")||header.querySelector("#settingsBtn");
  if(anchor&&anchor.parentNode)anchor.parentNode.insertBefore(btn,anchor);else header.appendChild(btn);
  if(isHelp)Array.prototype.forEach.call(document.querySelectorAll("header.site .nav-cta, header.site .nav-cta-m, header.site .nav-cta-sm"),function(el){el.style.display="none"});
  if(/[?&]focus=1/.test(location.search)){var b=box();if(b)setTimeout(function(){try{b.focus()}catch(err){}},250)}
})();
