import scrapy
import json
import os

class BookingSpider(scrapy.Spider):
    name = 'booking'
    start_urls = [
    'https://www.booking.com/',
    'https://www.booking.com/hotel/de/quot-la-mirabelle-quot.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE&sid=dde409912f03cd4d62292e2152e19831',
    'https://www.booking.com/hotel/de/landhotel-bohrerhof.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE&sid=dde409912f03cd4d62292e2152e19831',
    'https://www.booking.com/hotel/at/4rest-hall.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE',
    'https://www.booking.com/hotel/at/die-berge-lifestyle-solden.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE&sid=dde409912f03cd4d62292e2152e19831',
    'https://www.booking.com/hotel/at/restaurant-hirschen-haselstauden.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE&sid=dde409912f03cd4d62292e2152e19831',
    'https://www.booking.com/hotel/de/hornstein.de.html?aid=304142&label=gen173nr-1FCAMoDkINaGFsbC1pbi10aXJvbEgHWARoDogBAZgBB7gBB8gBDNgBAegBAfgBAogCAagCA7gCkaH4sAbAAgHSAiQ2OWVhYzdlOC0yZDE4LTQyMjItYTEyYy02OTI5YmVlYzg2YTPYAgXgAgE&sid=dde409912f03cd4d62292e2152e19831'
    ]  


    def parse(self, response):
        schema_annotations = response.css('script[type="application/ld+json"]::text').extract()

        schema_data = []
        for annotation in schema_annotations:
            try:
                data = json.loads(annotation)
                schema_data.append(data)
            except:
                continue

        # Create the 'output' directory if it doesn't exist
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        url_filename = response.url.split('/')[-1].split('?')[0] + '_schema.json'
        filename = os.path.join(output_dir, url_filename)
        with open(filename, 'w') as f:
            json.dump(schema_data, f, indent=4)

        self.log(f'Saved {len(schema_data)} items to {filename}')
