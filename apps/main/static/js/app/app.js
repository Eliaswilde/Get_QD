var app = angular.module("app",
    [
        'ui.bootstrap'
    ]);


app.config(function($locationProvider, $interpolateProvider, $httpProvider){

	$httpProvider.defaults.headers.post['X-CSRFToken'] = $('[name="csrfmiddlewaretoken"]:eq(0)').val();
//	$httpProvider.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

	$locationProvider.html5Mode(false);

	// Change start and end to work with Django
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');

});
