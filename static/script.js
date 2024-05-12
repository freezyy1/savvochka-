$(document).ready(function() {
  $.ajax({
    url: '/get_flowers', // Маршрут Flask для получения списка цветов
    method: 'GET',
    success: function(response) {
      displayFlowers(response);
    },
    error: function(xhr, status, error) {
      console.error(xhr.responseText);
    }
  });

  // Функция для отображения списка цветов
  function displayFlowers(flowers) {
    var flowersList = $('#flowersList');
    flowersList.empty();
    $.each(flowers, function(index, flower) {
      var flowerRow = $('<tr class="flower-row"></tr>');
      flowerRow.append('<td>' + flower.name + '</td>');
      flowerRow.append('<td>' + flower.type + '</td>');
      flowerRow.append('<td>' + flower.country + '</td>');
      flowerRow.append('<td>' + flower.season + '</td>');
      flowerRow.append('<td>' + flower.sort + '</td>');
      flowerRow.append('<td>' + flower.price + '</td>');
      flowersList.append(flowerRow);
    });
  }

  $.ajax({
    url: '/get_suppliers', // Маршрут Flask для получения списка поставщиков
    method: 'GET',
    success: function(response) {
      displaySuppliers(response);
    },
    error: function(xhr, status, error) {
      console.error(xhr.responseText);
    }
  });

  function displaySuppliers(suppliers) {
    var suppliersList = $('#suppliersList');
    suppliersList.empty();
    $.each(suppliers, function(index, supplier) {
      var supplierRow = $('<tr></tr>');
      supplierRow.append('<td>' + supplier.name + '</td>');
      supplierRow.append('<td>' + supplier.type + '</td>');
      supplierRow.append('<td>' + supplier.address + '</td>');
      suppliersList.append(supplierRow);
    });
  }

  $.ajax({
    url: '/get_sellers', // Маршрут Flask для получения списка продавцов
    method: 'GET',
    success: function(response) {
      displaySellers(response);
    },
    error: function(xhr, status, error) {
      console.error(xhr.responseText);
    }
  });

  function displaySellers(sellers) {
    var sellersList = $('#sellersList');
    sellersList.empty();
    $.each(sellers, function(index, seller) {
      var sellerRow = $('<tr></tr>');
      sellerRow.append('<td>' + seller.name + '</td>');
      sellerRow.append('<td>' + seller.address + '</td>');
      sellersList.append(sellerRow);
    });
  }

  function getFlowersBySeason() {
    var season = $('#seasonSelect').val();
    $.ajax({
      url: '/filter_by_season/' + season, // Маршрут Flask для фильтрации цветов по сезону
      method: 'GET',
      success: function(response) {
        displayFlowers(response);
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
      }
    });
  }

  function getFlowersByCountry() {
    var country = $('#countryInput').val();
    $.ajax({
      url: '/filter_by_country/' + country, // Маршрут Flask для фильтрации цветов по стране
      method: 'GET',
      success: function(response) {
        displayFlowers(response);
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
      }
    });
  }
});
