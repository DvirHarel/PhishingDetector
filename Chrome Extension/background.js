
const port = 3000;
const server = `http://localhost:${port}`;

chrome.tabs.onUpdated.addListener((tabId,changeInfo,tab) => {
    if(tab.url !== undefined && changeInfo.status == "complete"){
        if(!`${tab.url}`.startsWith("chrome://"))
            fetch(server.concat(`?url=${tab.url}`)).then(r => r.text()).then(result => {
            if (result == 1){
                console.log("This webpage is Phishing you!")
                window.alert(`This webpage is Phishing you! \n ${tab.url}`)
            }
            else{
                console.log("This webpage is not Phishing!")       
            }    
        })
    };
}
)



           
