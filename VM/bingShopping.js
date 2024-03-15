https://www.msn.com/en-us/shopping

// Original
javascript: (() => { var msnShoppingGamePane = document.querySelector("shopping-page-base")    ?.shadowRoot.querySelector("shopping-homepage")    ?.shadowRoot.querySelector("msft-feed-layout")    ?.shadowRoot.querySelector("msn-shopping-game-pane"); if(msnShoppingGamePane != null){    msnShoppingGamePane.cardsPerGame = 1;    msnShoppingGamePane.resetGame();}else alert("Unable to locate the shopping game!");})();

// Top
javascript: (() => { var msnShoppingGamePane = document.querySelector("shopping-page-base")    ?.shadowRoot.querySelector("shopping-homepage")    ?.shadowRoot.querySelector("msft-feed-layout")    ?.shadowRoot.querySelector("msn-shopping-game-pane"); if(msnShoppingGamePane != null){   msnShoppingGamePane.style.setProperty("grid-area", "slot1");    msnShoppingGamePane.cardsPerGame = 1;    msnShoppingGamePane.resetGame();}else alert("Unable to locate the shopping game!");})();



javascript: (() => { document.querySelector('.shopping-select-overlay-button').click();})();


// Select
javascript: (() => { var msnShoppingGamePane = document.querySelector("shopping-page-base")    ?.shadowRoot.querySelector("shopping-homepage")    ?.shadowRoot.querySelector("msft-feed-layout")    ?.shadowRoot.querySelector("msn-shopping-game-pane"); if(msnShoppingGamePane != null){   msnShoppingGamePane.style.setProperty("grid-area", "slot1");    msnShoppingGamePane.cardsPerGame = 1;    msnShoppingGamePane.resetGame();}else alert("Unable to locate the shopping game!");})();



<button class="shopping-select-overlay-button" data-t="{&quot;n&quot;:&quot;find-best-deal-select-button|personalized:0&quot;,&quot;t&quot;:12,&quot;a&quot;:&quot;click&quot;,&quot;b&quot;:56,&quot;c.v&quot;:&quot;shopping&quot;,&quot;c.c&quot;:&quot;shopping&quot;}">Select</button>


document.getElementById('elementID').click();


<button class="shopping-select-overlay-button" data-t="{&quot;n&quot;:&quot;find-best-deal-select-button|personalized:0&quot;,&quot;t&quot;:12,&quot;a&quot;:&quot;click&quot;,&quot;b&quot;:56,&quot;c.v&quot;:&quot;shopping&quot;,&quot;c.c&quot;:&quot;shopping&quot;}">Select</button>


shadowRoot.querySelector('.shopping-select-overlay-button').click();


javascript: (() => { var selectClick = driver.findElement(By.xpath("/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]")).click;})();


/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]


//*[@id="61072042747"]/div/div/button[1]


javascript: (() => { var xPathRes = document.evaluate ('/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
xPathRes.singleNodeValue.click();})();


document.evaluate(" //a[ contains(@src, 'msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]') ] ", document.body, null, 9, null). singleNodeValue.click();  


javascript: (() => { var xPathRes = document.evaluate(" //a[ contains(@src, 'msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]') ] ", document.body, null, 9, null). singleNodeValue.click();})();



    var button;
    try{  // Xpath for most browsers
    button = document.evaluate(".//input[ contains(@id, 'msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]') ] ", document.body, null, 9, null). singleNodeValue;
    }catch(err){  // DOM method for IE8 and below
    button = document.getElementById("someID"); 
    }


    driver.findElement(By.xpath("/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]")).click;


    javascript: (() => { var xPathRes = driver.findElement(By.xpath("/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]"));
    xPathRes.click();})();


    javascript: (() => { var xResults = document.evaluate("/html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card/msn-shopping-card/div/div/button[1]", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null); var url = xResults.snapshotItem(0).href; window.open(url);})();


    //*[@id="120065182447"]/div/div/button[1]
    //*[@id="102501407849"]/div/div/button[1]
    
    driver.find_element_by_link_text("Select").click()




    javascript: (() => { driver.find_element_by_link_text("Select").click();})();
    javascript: (() => { PathRes = document.getElementsByClassName('shopping-select-overlay-button').click();})();



    getElementsByClassName('pl-video-edit-remove')
    var button = document.getElementById('shopping-select-overlay-button');
    button.form.submit();

    document.getElementById('clickButton').click();


    var button = document.getElementById('clickButton');
    button.form.submit();




    javascript:for(var i=0; i<(document.getElementsByTagName('a')).length; i++) {(document.getElementsByTagName('a')[i]).style.pointerEvents = 'none';}function handler(e) {e = e || window.event;var target = e.target || e.srcElement;target.style.display = 'none';document.removeEventListener('click', handler, false);cursor('default');for(var i=0; i<(document.getElementsByTagName('a')).length; i++) {(document.getElementsByTagName('a')[i]).style.pointerEvents = 'initial';}}document.addEventListener('click', handler, false);cursor('crosshair');function cursor(cur) { document.body.style.cursor = cur; }


    pointerEvents = 'none';}function handler(e) {e = e || window.event;var target = e.target || e.srcElement;target.style.display = 'none';document.removeEventListener('click', handler, false);cursor('default');for(var i=0; i<(document.getElementsByTagName('a')).length; i++) {(document.getElementsByTagName('a')[i]).style.pointerEvents = 'initial';}}document.addEventListener('click', handler, false);cursor('crosshair');function cursor(cur) { document.body.style.cursor = cur; }



    document.querySelector("#root > div > div > fluent-design-system-provider > div > div:nth-child(4) > div > shopping-page-base").shadowRoot.querySelector("div > div.shopping-page-content > shopping-homepage").shadowRoot.querySelector("div > msft-feed-layout").shadowRoot.querySelector("msn-shopping-game-pane").shadowRoot.querySelector("#\\33 1935266857 > div > div > button.shopping-select-overlay-button")


    javascript:document.getElementsByClassName("shopping-deals").click()


    <button class="shopping-select-overlay-button" data-t="{&quot;n&quot;:&quot;find-best-deal-select-button|personalized:0&quot;,&quot;t&quot;:12,&quot;a&quot;:&quot;click&quot;,&quot;b&quot;:56,&quot;c.v&quot;:&quot;shopping&quot;,&quot;c.c&quot;:&quot;shopping&quot;}">Select</button>


    /html/body/div/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card

    //*[@id="root"]/div/div/fluent-design-system-provider/div/div[4]/div/shopping-page-base//div/div[2]/shopping-homepage//div/msft-feed-layout//msn-shopping-game-pane//div[2]/msft-stripe/div/fluent-card



    handleEvent(t) {
        const e = t.currentTarget[this.data];
        if (e.isBound) {
          s.rd.setEvent(t);
          const n = this.dataBinding.evaluate(e.source, e.context);
          s.rd.setEvent(null), !0 !== n && t.preventDefault()
        }
      }


      handleEvent(t) {
        const e = t.currentTarget[this.data];
        if (e.isBound) {
          s.rd.setEvent(t);
          const n = this.dataBinding.evaluate(e.source, e.context);
          s.rd.setEvent(null), !0 !== n && t.preventDefault()
        }
      }
