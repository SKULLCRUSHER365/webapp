    
        //this is for currency so it will always same for everyone that's why i wrote it here
        fetch('http://127.0.0.1:8000/currency/')
            .then(response => response.json())
            .then(data => {
                var newoption = document.createElement("option");
                newoption.innerHTML = "--select--";
                document.getElementById("currency").options.add(newoption);
                for (option in data) {
                    var newoption = document.createElement("option");
                    newoption.value = `${data[option].id}`;
                    newoption.innerHTML = `${data[option].symbol}`;
                    document.getElementById("currency").options.add(newoption);
                }
            });



        //this funtion is made to reset the whole display and only show the first scroll down list
        function display1(s1) {
            var selects = document.getElementsByTagName("select");
            var inputs = document.getElementsByTagName("input");

            for (x of selects) {
                x.style.display = 'none';
            }
            for (x of inputs) {
                if(!x.type==="hidden"){
                x.style.display = 'none';
            }}
            document.getElementById(s1).style.display = 'block';
        }
        //this function is to reset the form if the second scroll down list has any change in it
        function display2(s1, s2) {
            var selects = document.getElementsByTagName("select");
            var inputs = document.getElementsByTagName("input");

            for (x of selects) {
                x.style.display = 'none';
            }
            for (x of inputs) {
                if(!x.type==="hidden"){
                x.style.display = 'none';
                x.value = '';}
            }
            document.getElementById(s1).style.display = 'block';
            document.getElementById(s2).style.display = 'block';

        }



        // this is for the first option that we gonna select
        // this will be called when the first scrolldown list gona change so i just have to reset all the content of the page exept the
        // first list and recall this function so it will display the second list

        function first(s1, s2) {
            display1(s1);
            console.log("hello world");
            var s1 = document.getElementById(s1);
            var s2 = document.getElementById(s2);
            s2.innerHTML = '';
            s2.style.display = 'block';


            fetch('http://127.0.0.1:8000/selection/')
                .then(response => response.json())
                .then(data => {
                    var newoption = document.createElement("option");
                    newoption.innerHTML = "--select--";
                    s2.options.add(newoption);
                    for (option in data) {
                        var newoption = document.createElement("option");
                        if (data[option].catagory == s1.value) {
                            newoption.value = `${data[option].id}`;
                            newoption.innerHTML = `${data[option].subcatagory1}`;
                            s2.options.add(newoption);
                        }
                    }
                });
        }




        // this is the function which will be called when there is anyh selection change i the second scroll down list 
        // so in this display2 fuction will be called first so that whenver it is changed that second scrooll down list 
        // the all things disappear except the first and second scrolll down list

        function second(s1, s2, s3, s4) {
            display2("firstentry", s1);

            var s1 = document.getElementById(s1);
            var s2 = document.getElementById(s2);
            var s3 = document.getElementById(s3);
            var s4 = document.getElementById(s4);
            s2.innerHTML = '';

            // this is for whenever user selects wafers or substrate
            if ('1' == s1.value || '2' == s1.value) {
                s2.style.display = 'block';
                s3.style.display = 'none';
                fetch('http://127.0.0.1:8000/selection/')
                    .then(response => response.json())
                    .then(data => {
                        var newoption = document.createElement("option");
                        newoption.innerHTML = "--select--";
                        s2.options.add(newoption);
                        for (option in data) {
                            var newoption = document.createElement("option");
                            if (data[option].catagory == 'substrateorwafers') {
                                newoption.value = `${data[option].id}`;
                                newoption.innerHTML = `${data[option].subcatagory1}`;
                                s2.options.add(newoption);

                            }
                        }
                    });
                    var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';
            }
            else if ('5' == s1.value) {
                s2.style.display = 'block';
                s3.style.display = 'none';
                fetch('http://127.0.0.1:8000/selection/')
                    .then(response => response.json())
                    .then(data => {
                        var newoption = document.createElement("option");
                        newoption.innerHTML = "--select--";
                        s2.options.add(newoption);
                        for (option in data) {
                            var newoption = document.createElement("option");
                            if (data[option].catagory == 'gases') {
                                newoption.value = `${data[option].id}`;
                                newoption.innerHTML = `${data[option].subcatagory1}`;
                                s2.options.add(newoption);
                            }
                        }
                    });
                    var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';
            }
            else if ('6' == s1.value) {
                s2.style.display = 'block';
                s3.style.display = 'none';
                fetch('http://127.0.0.1:8000/selection/')
                    .then(response => response.json())
                    .then(data => {
                        var newoption = document.createElement("option");
                        newoption.innerHTML = "--select--";
                        s2.options.add(newoption);
                        for (option in data) {
                            var newoption = document.createElement("option");
                            if (data[option].catagory == 'labsupplies') {
                                newoption.value = `${data[option].id}`;
                                newoption.innerHTML = `${data[option].subcatagory1}`;
                                s2.options.add(newoption);
                            }
                        }
                    });
                    var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';
            }
            else if ('9' == s1.value) {
                s2.style.display = 'block';
                s3.style.display = 'none';
                fetch('http://127.0.0.1:8000/selection/')
                    .then(response => response.json())
                    .then(data => {
                        var newoption = document.createElement("option");
                        newoption.innerHTML = "--select--";
                        s2.options.add(newoption);
                        for (option in data) {
                            var newoption = document.createElement("option");
                            if (data[option].catagory == 'softwarelicence') {
                                newoption.value = `${data[option].id}`;
                                newoption.innerHTML = `${data[option].subcatagory1}`;
                                s2.options.add(newoption);
                            }
                        }
                    });
                    var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';
            }
            else if ('3' == s1.value || '4' == s1.value || '7' == s1.value) {
                s3.style.display = 'block';
                s2.style.display = 'none';
                s4.innerHTML = '';

                if (s1.value == '3' || s1.value == '4') {
                    fetch('http://127.0.0.1:8000/compounds/')

                        .then(response => response.json())
                        .then(data => {
                            console.log(data);
                            for (option in data) {
                                var newoption = document.createElement("option");
                                newoption.value = `${data[option].casrn} (${data[option].chemicalformulla})`;
                                newoption.innerHTML = `${data[option].compoundname}`;
                                s4.appendChild(newoption);
                                document.getElementById("MSDS").style.display = 'block';
                            }


                        });
                }
                var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';
            }



        }

        function Thirdselection(s1, s2) {
            var s1 = document.getElementById(s1);
            var s2 = document.getElementById(s2);
            s2.style.display = 'none';

            if (s1.value == '17' || s1.value == '28' || s1.value == '34' || s1.value == '35' || s1.value == '36') {
                s2.style.display = 'block';
            }
            var foo = document.getElementsByClassName("Unit");
                foo[0].style.display = 'block';
                foo[1].style.display = 'block'; foo[2].style.display = 'block'; foo[3].style.display = 'block';
                foo[4].style.display = 'block'; foo[5].style.display = 'block';foo[6].style.display='block';




        }






        //testing

        function popupfunc() {
        window.open("popup","popup_page","status=1,height:300,width:600,toolbar=0,resizeable=0")}
      