require 'test_helper'

class StaticPagesControllerTest < ActionDispatch::IntegrationTest
  test "should get home" do
    get static_pages_home_url
    assert_response :success
  end

  test "should get randomimage" do
    get static_pages_randomimage_url
    assert_response :success
  end

  test "should get whitenoise" do
    get static_pages_whitenoise_url
    assert_response :success
  end

  test "should get rsa" do
    get static_pages_rsa_url
    assert_response :success
  end

end
