package drechslr.spotify1;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;


import com.wrapper.spotify.Api;
import com.wrapper.spotify.methods.AlbumRequest;
import com.wrapper.spotify.methods.AlbumsForArtistRequest;
import com.wrapper.spotify.methods.FeaturedPlaylistsRequest;
import com.wrapper.spotify.methods.PlaylistRequest;
import com.wrapper.spotify.methods.PlaylistTracksRequest;
import com.wrapper.spotify.methods.RelatedArtistsRequest;
import com.wrapper.spotify.methods.UserPlaylistsRequest;
import com.wrapper.spotify.methods.authentication.ClientCredentialsGrantRequest;
import com.wrapper.spotify.models.Album;
import com.wrapper.spotify.models.Artist;
import com.google.common.util.concurrent.FutureCallback;
import com.google.common.util.concurrent.Futures;
import com.google.common.util.concurrent.SettableFuture;
import com.wrapper.spotify.models.ClientCredentials;
import com.wrapper.spotify.models.FeaturedPlaylists;
import com.wrapper.spotify.models.Page;
import com.wrapper.spotify.models.Playlist;
import com.wrapper.spotify.models.PlaylistTrack;
import com.wrapper.spotify.models.PlaylistTracksInformation;
import com.wrapper.spotify.models.SimpleAlbum;
import com.wrapper.spotify.models.SimplePlaylist;
import com.wrapper.spotify.models.SimpleTrack;
import com.wrapper.spotify.models.Track;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
       
        final String clientId = "fbf0790d1c5d48ba93eea49def331076";
        final String clientSecret = "8e3a843de8e546f3a2ae11b892f4b2fc";

        final Api api = Api.builder()
          .clientId(clientId)
          .clientSecret(clientSecret)
          .build();

        /* Create a request object. */
        final ClientCredentialsGrantRequest request = api.clientCredentialsGrant().build();

        /* Use the request object to make the request, either asynchronously (getAsync) or synchronously (get) */
        final SettableFuture<ClientCredentials> responseFuture = request.getAsync();
        
        /* Add callbacks to handle success and failure */
        Futures.addCallback(responseFuture, new FutureCallback<ClientCredentials>() {
          public void onSuccess(ClientCredentials clientCredentials) {
            /* The tokens were retrieved successfully! */
            System.out.println("Successfully retrieved an access token! " + clientCredentials.getAccessToken());
            System.out.println("The access token expires in " + clientCredentials.getExpiresIn() + " seconds");
            
            /* Set access token on the Api object so that it's used going forward */
            api.setAccessToken(clientCredentials.getAccessToken());
 
            /* Please note that this flow does not return a refresh token.
           * That's only for the Authorization code flow */
          }

          public void onFailure(Throwable throwable) {
            /* An error occurred while getting the access token. This is probably caused by the client id or
             * client secret is invalid. */
          }
        });
        
        ///Authentification done 
        
        //set up Lists
        
        //return value
        List<String> outputTracklist = new ArrayList<String>();
        
        //Saved as ID:
        //List of artists used for searching related artists
        List<String> searchProcessedArtists = new ArrayList<String>();
        //List of artists usable for searching related artists
        List<String> searchUnprocessedArtists = new ArrayList<String>(); 
        //List with artists whom tracks are alrdy in Output-Tracklist
        List<String> processedArtists = new ArrayList<String>();
        
        //variable parts
        int minimumSizeOutputList = 50000;
        String startArtistUri = "1BOTcSZvfl1F4kui1f95dk";//"7dGJo4pcD2V6oG8kP0tJRR"; //"3g2kUQ6tHLLbmkV7T4GPtL";
        
        //the loop
        searchUnprocessedArtists.add(startArtistUri);
        int testiterationLimit = 0;
        
        do {
        		//request rel.Artists for an Artist in searchUnprocessedArtists
        		System.out.println("search request for "+searchUnprocessedArtists.get(0));
        		RelatedArtistsRequest artReq = api.getArtistRelatedArtists(searchUnprocessedArtists.get(0)).build();
        		try {
        			List<Artist> artists = artReq.get();
        			for (Artist artist : artists) {
        				String artistId = artist.getId();
        				if (!processedArtists.contains(artistId)) {
        					//append artist to searchUnprocessed 
        					searchUnprocessedArtists.add(artistId);
        					//process the artist
        					//for the moment: just print out the artist name
        					System.out.println("Here will be listed some Tracks from " + artist.getName());
        					//do it.
        					//request artists albums
        					AlbumsForArtistRequest albumForArtReq = api.getAlbumsForArtist(artistId).build();
        					try {
        						Page<SimpleAlbum> simpleAlbumPage = albumForArtReq.get();
        						List<SimpleAlbum> simpleAlbums = simpleAlbumPage.getItems();
        						for (SimpleAlbum simpleAlbum : simpleAlbums) {
        							String albumId = simpleAlbum.getId();
        							//request the full album info
        							AlbumRequest albumReq = api.getAlbum(albumId).build();
        							try {
        								Album album = albumReq.get();
        								Page<SimpleTrack> tracksPage= album.getTracks();
        								List<SimpleTrack> tracks = tracksPage.getItems();
        								for (SimpleTrack track : tracks) {
        									String trackId = track.getId();
        									System.out.println(trackId);
        									outputTracklist.add(trackId);
        								}
        							}catch (Exception e) {
                						System.out.println("Failed getting Album" + albumId);	
                						Thread.sleep(2000);
        							}
        						}
        							
        					}catch (Exception e) {
        						System.out.println("Failed getting Albums for Artist" + artist.getName() + " ("+artistId +") ");
        						Thread.sleep(2000);
        					}
        					
        					
        					//add them to processed 
        					processedArtists.add(artistId);
        				}
        			}
        			//handle the Artist used for relatedSearch
        			searchProcessedArtists.add(searchUnprocessedArtists.get(0));
        			searchUnprocessedArtists.remove(0);
        			Thread.sleep(2000);
        		}catch (Exception e) {
        			System.out.println("Failed getting related Artists for " + searchUnprocessedArtists.get(0));
        			searchUnprocessedArtists.remove(0);
        			///REPAIR STUFF HERE
        		}
        		testiterationLimit += 1;
        		
        	
        } while (outputTracklist.size()<=minimumSizeOutputList && (!searchUnprocessedArtists.isEmpty()));
        
        System.out.println("iterations: "+ testiterationLimit);
        
        PrintWriter writer;
		try {
			writer = new PrintWriter("the-file-name.txt", "UTF-8");
	        for (String output : outputTracklist) {
	        		writer.println(output);
	        }
	        writer.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}
