var testApp = angular.module('testApp', []);

testApp.controller('PhoneListCtrl', function($scope){
    $scope.phones = [
        {'name': 'Nexus S',
        'snippet': 'Fast just got faster with Nexus S.'},
        {'name': 'Motorola XOOM with Wi-Fi',
        'snippet': 'The Next, Next Generation tablet.'},
        {'name': 'MOTOROLA XOOM',
        'snippet': 'The Next, Next Generation tablet.'}
    ];
});

testApp.controller('FruitListCtrl', function($scope){
    $scope.fruits = [
        {'name': 'apple', 'color': 'red', 'no': 2},
        {'name': 'grape', 'color': 'violet', 'no': 3},
        {'name': 'orange', 'color': 'orange', 'no': 1}
    ];
    $scope.orderProp = 'no';
});

testApp.controller('DrinkListCtrl', function ($scope, $http) {
    $http.get('drink.json').success(function(data) {
        $scope.drinks = data;
    });

    $scope.orderProp = 'no';
});
