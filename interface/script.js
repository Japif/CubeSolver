const spigols = [
    ['ub', 'ft'],
    ['ut', 'bt'],
    ['uml', 'lt'],
    ['umr', 'rt'],
    ['fml', 'lmr'],
    ['fmr', 'rml'],
    ['fb', 'dt'],
    ['rb', 'dmr'],
    ['rmr', 'bml'],
    ['lb', 'dml'],
    ['lml', 'bmr'],
    ['bb', 'db']
]

const angles = [
    ['utl', 'ltl', 'btr'],
    ['utr', 'rtr', 'btl'],
    ['ubl', 'ftl', 'ltr'],
    ['ubr', 'ftr', 'rtl'],
    ['dtl', 'fbl', 'lbr'],
    ['dtr', 'fbr', 'rbl'],
    ['dbl', 'lbl', 'bbr'],
    ['dbr', 'rbr', 'bbl']
]

const spDict = [
    {
        'w': '12',
        'g': '62'
    },
    {
        'w': '14',
        'r': '42'
    },
    {
        'w': '16',
        'o': '52'
    },
    {
        'w': '18',
        'b': '22'
    },
    {
        'b': '24',
        'r': '46'
    },
    {
        'b': '26',
        'o': '54'
    },
    {
        'g': '64',
        'o': '56'
    },
    {
        'g': '66',
        'r': '44'
    },
    {
        'y': '32',
        'b': '28'
    },
    {
        'y': '34',
        'r': '48'
    },
    {
        'y': '36',
        'o': '58'
    },
    {
        'y': '38',
        'g': '68'
    }
]
const agDict = [
    {
        'w': '11',
        'r': '41',
        'g': '63'
    },
    {
        'w': '13',
        'o': '53',
        'g': '61'
    },
    {
        'w': '17',
        'b': '21',
        'r': '43'
    },
    {
        'w': '19',
        'b': '23',
        'o': '51'
    },
    {
        'y': '31',
        'b': '27',
        'r': '49'
    },
    {
        'y': '33',
        'b': '29',
        'o': '57'
    },
    {
        'y': '37',
        'r': '47',
        'g': '69'
    },
    {
        'y': '39',
        'o': '59',
        'g': '67'
    }
]
$('.cube').click(function () {
    if (!$(this).hasClass('center')){
        $(this).attr('class', '');
        $(this).addClass('cube').addClass($('#colors').val());
        $(this).attr('color', $('#colors').val());
    }
});

function iterateAngles(){
    angles.forEach(function (block) {
        let tempArray = [];
        block.forEach(function (sticker) {
            tempArray.push($(`#${sticker}`).attr('color'));
        });
        agDict.forEach(function (dict) {
            let tempDict = [];
            for (const [key, value] of Object.entries(dict)) {
                tempDict.push(key);
            }
            if (tempDict.sort().toString() === tempArray.sort().toString()){
                block.forEach(function (sticker) {
                    let genColor = $(`#${sticker}`).attr('color');
                    $(`#${sticker}`).attr('name', dict[genColor]);
                });
            }
        });
    });
}
function iterateSpiglos(){
    spigols.forEach(function (block) {
        let tempArray = [];
        block.forEach(function (sticker) {
            tempArray.push($(`#${sticker}`).attr('color'));
        });
        spDict.forEach(function (dict) {
            let tempDict = [];
            for (const [key, value] of Object.entries(dict)) {
                tempDict.push(key);
            }
            if (tempDict.sort().toString() === tempArray.sort().toString()){
                block.forEach(function (sticker) {
                    let genColor = $(`#${sticker}`).attr('color');
                    $(`#${sticker}`).attr('name', dict[genColor]);
                });
            }
        });
    });
}

$('#button').click(function () {
    iterateSpiglos();
    iterateAngles();
});

$('#gather').click(function () {
    const totArray = []
    $(".cube").each(function () {
        totArray.push($(this).attr('name'));
    });
    let index = 0;
    let upFace = [];
    let leftFace = [];
    let frontFace = [];
    let rightFace = [];
    let backFace = [];
    let downFace = [];
    totArray.forEach(function (number) {
        number = parseInt(number);
        if (index < 9) {
            upFace.push(number);
        }
        else if (index>=9 && index < 18){
            leftFace.push(number);
        }
        else if (index>=18 && index < 27){
            frontFace.push(number);
        }
        else if (index>=27 && index < 36){
            rightFace.push(number);
        }
        else if (index>=36 && index < 45){
            backFace.push(number);
        }
        else if (index >=45){
            downFace.push(number);
        }

        index = index + 1;
    });
    const fillerArray = [0,0,0]
    const array1 = fillerArray.concat(upFace.slice(0, 3), fillerArray, fillerArray);
    const array2 = fillerArray.concat(upFace.slice(3, 6), fillerArray, fillerArray);
    const array3 = fillerArray.concat(upFace.slice(6, 9), fillerArray, fillerArray);
    const array4 = leftFace.slice(0, 3).concat(frontFace.slice(0, 3), rightFace.slice(0, 3), backFace.slice(0, 3));
    const array5 = leftFace.slice(3, 6).concat(frontFace.slice(3, 6), rightFace.slice(3, 6), backFace.slice(3, 6));
    const array6 = leftFace.slice(6, 9).concat(frontFace.slice(6, 9), rightFace.slice(6, 9), backFace.slice(6, 9));
    const array7 = fillerArray.concat(downFace.slice(0, 3), fillerArray, fillerArray);
    const array8 = fillerArray.concat(downFace.slice(3, 6), fillerArray, fillerArray);
    const array9 = fillerArray.concat(downFace.slice(6, 9), fillerArray, fillerArray);
    console.log(array1);
    console.log(array2);
    console.log(array3);
    console.log(array4);
    console.log(array5);
    console.log(array6);
    console.log(array7);
    console.log(array8);
    console.log(array9);
});